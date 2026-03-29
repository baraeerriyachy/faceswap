# InsightFace Real-Time Face Swap

## 🛠 Setup

### 1. Download model
```
wget -O inswapper_128.onnx https://github.com/facefusion/facefusion-assets/releases/download/models/inswapper_128.onnx
```

### 2. Add source image
- Put your face image in the folder  
- Name it: image.jpg

## 📦 Install
```
pip install insightface onnxruntime opencv-python
```

## 🚀 Run
```
python run.py
```

## ⌨️ Controls
- q → quit  
- camera index → change in code (VideoCapture(0))

