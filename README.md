# InsightFace Real-Time Face Swap

## 🛠 Setup

### 1. Download model
wget -O inswapper_128.onnx https://github.com/facefusion/facefusion-assets/releases/download/models/inswapper_128.onnx

### 2. Add source image
- Put your face image in the folder  
- Name it: image.jpg

## 📦 Install
pip install insightface onnxruntime-openvino opencv-python numpy

# Arch fix:
sudo pacman -S python-opencv

## 🚀 Run
python run.py

## ⚙️ Features
- Frame skipping (real-time CPU)
- Live face swap (InsightFace)
- OpenVINO (Intel acceleration)
- Mirror webcam view
- Low latency (buffer = 1)

## ⌨️ Controls
- q → quit  
- camera index → change in code (VideoCapture(0))

## 📁 Required files
run.py
image.jpg
inswapper_128.onnx

## ⚠️ Notes
- Use 640x480 or lower for best FPS  
- Works best with 1 face  
- Intel GPU → enabled via OpenVINO  
