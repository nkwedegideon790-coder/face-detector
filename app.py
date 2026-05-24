import torch

# 1. Grab PyTorch's native load function
_original_load = torch.load

# 2. Build a wrapper that intercepts all calls and explicitly forces weights_only=False
def _permissive_torch_load(*args, **kwargs):
    kwargs['weights_only'] = False
    return _original_load(*args, **kwargs)

# 3. Hijack the global function completely
torch.load = _permissive_torch_load

import cv2
import supervision as sv
import uvicorn
import torch
from fastapi import FastAPI,UploadFile,File
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import uuid

from ultralytics import YOLO
               
app = FastAPI()
model = YOLO('yolov8n.pt')
tracker = sv.ByteTrack()
circle_annonator = sv.BoxAnnotator()
label_annonator = sv.LabelAnnotator()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)
INPUT_DIR = '../uploads'
OUTPUT_DIR = '../uploads'
os.makedirs(INPUT_DIR,exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True) 

@app.post('/detect')
async def Generate_frame(file:UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    input_path = os.path.join(INPUT_DIR, f'{file_id}_{file.filename}')
    output_path = os.path.join(OUTPUT_DIR, f'processed video_{file_id}.mp4')
    with open(input_path, 'wb') as f:
        f.write(await file.read())
    cap = cv2.VideoCapture(input_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width,height))
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)[0]
        detections = sv.Detections.from_ultralytics(results)
        detections = tracker.update_with_detections(detections)

        labels = [f'#{tid}' for tid in detections.tracker_id]

        annonated_frame = circle_annonator.annotate(scene=frame ,detections=detections)
        annonated_frame = label_annonator.annotate(scene=annonated_frame, detections=detections,
                                                    labels=labels)
        out.write(annonated_frame)
    
    cap.release()
    out.release()

    def iterfile():
        with open(output_path, 'rb') as f:
            yield from f
    return StreamingResponse(iterfile(),
                             media_type='video/mp4')


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

