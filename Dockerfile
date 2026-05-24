# official python images
FROM python:3.10_slim

# set work dir
WORKDIR /app

# install system deps for opencv + ultralytics
RUN apt-get update && apt-get install -y \ 
    libgl1-mesa-glx \
    libglib2.0_0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY yolo12n-face.pt .

EXPOSE 8000
CMD [ "uvicrn", "app:app", "--host", "0.0.0.0", "--port", "8000" ]
