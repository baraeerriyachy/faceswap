import os
import cv2
import insightface
from insightface.app import FaceAnalysis

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ["QT_QPA_PLATFORM"] = "xcb"

app = FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(320, 320))
swapper = insightface.model_zoo.get_model('inswapper_128.onnx', download=False)

source_img = cv2.imread("image.jpg")
source_face = app.get(source_img)[0]

cap = cv2.VideoCapture(2)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

frame_count = 0
last_frame = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    if frame_count % 3 == 0:
        faces = app.get(frame)
        for face in faces:
            frame = swapper.get(frame, face, source_face, paste_back=True)
        last_frame = frame.copy()
    elif last_frame is not None:
        frame = last_frame
    cv2.imshow('Face Swap', frame)
    frame_count += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
