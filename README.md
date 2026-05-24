![Preview](./preview.png)
📷 SMART FACE DETECTOR SYSTEM

a high performance computer vision pipeline design to detect a person, track  with a real_time integrated fast_api for remote control

KEY FEATURES

Object Detection: powered by YOLOv11 for state of art accuracy

Multi-Object Tracking: uses byte track to maintain vehicles id across frame

video input : 

tech stack
 Tech Stack
 Component Technology Language Python
 3.9+ InferenceUltralytics YOLOv11Logic
 GeometrySupervision(by roboflow)Api
 Framwork FastAPI & uvicornimage Processing OpenCV

 🚀 Getting Started

 1 Installation

Bash

# Clone the repository git Clone

#install dependencies
pip install -r requirement.txt

2 configuration
open main.py and set video source
webcam: cap = cv2.videoCapture(0)
video File = cap = cv2.videocapture('walkway.mp4')

3
running the api

uvicorn.run(app, host= 0.0.0.0, port= 5000)

Api Endpoints

/detect = getlive annonated mjpeg video stream
/status = returns the status of the streaming

lologic visualization
the system detects human faces and starts tracking
class Filtering
the system is strictly configured to track  only faces of a person

🏄‍♂️Road map
 yolov11 integration
 real time tracking
 fast api streaming



