![Preview](./preview.png)

# 📷 SMART FACE DETECTOR SYSTEM

A high-performance computer vision pipeline designed to detect and track faces in real-time with an integrated FastAPI server for remote control and monitoring.

## ✨ Key Features

- **Object Detection**: Powered by YOLOv11 for state-of-the-art accuracy
- **Multi-Object Tracking**: Uses ByteTrack to maintain consistent face IDs across frames
- **Real-Time Streaming**: Live annotated MJPEG video stream via FastAPI
- **Remote Control**: API endpoints for monitoring and system status

## 🛠 Tech Stack

| Component                | Technology                |
| ------------------------ | ------------------------- |
| **Language**             | Python 3.9+               |
| **Detection**            | Ultralytics YOLOv11       |
| **Tracking**             | ByteTrack                 |
| **Geometry & Utilities** | Supervision (by Roboflow) |
| **API Framework**        | FastAPI & Uvicorn         |
| **Image Processing**     | OpenCV                    |

## 🚀 Getting Started

### 1. Installation

```bash
# Clone the repository
git clone <repository-url>

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

Edit `app.py` to set your video source:

```python
# For webcam:
cap = cv2.VideoCapture(0)

# For video file:
cap = cv2.VideoCapture('walkway.mp4')
```

### 3. Running the API

```bash
python app.py
```

Or manually run with uvicorn:

```bash
uvicorn app:app --host 0.0.0.0 --port 5000
```

## 📡 API Endpoints

| Endpoint  | Method | Description                          |
| --------- | ------ | ------------------------------------ |
| `/detect` | GET    | Live annotated MJPEG video stream    |
| `/status` | GET    | Returns the current streaming status |

## 🔍 How It Works

1. The system detects human faces in each frame using YOLOv11
2. Detected faces are tracked across frames using ByteTrack to maintain consistent IDs
3. The system is strictly configured to track only human faces
4. Annotated video with bounding boxes and tracking IDs is streamed in real-time

## 🗺 Roadmap

- [x] YOLOv11 integration
- [ ] Enhanced real-time tracking performance
- [ ] Improved FastAPI streaming optimization
