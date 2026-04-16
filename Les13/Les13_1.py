import cv2
from cvzone.FaceDetectionModule import (
    FaceDetector,
)

cap = cv2.VideoCapture(0)  # веб-камера
detector = FaceDetector(minDetectionCon=0.7)  # порог уверенности
while True:
    (
        success,
        img,
    ) = cap.read()
    (
        img,
        boxes,
    ) = detector.findFaces(img)  # boxes: список детекций
    cv2.imshow(
        "Head/Face Detection - cvzone",
        img,
    )
cap.release()
cv2.destroyAllWindows()
