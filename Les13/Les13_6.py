import cv2
from cvzone.FaceDetectionModule import (
    FaceDetector,
)

cap = cv2.VideoCapture("./../videoFace/132653-754103324_tiny.mp4")
detector = FaceDetector(minDetectionCon=0.7)

prev_box = None  # предыдущие координаты
movement = 5
while True:
    (
        success,
        img,
    ) = cap.read()
    (
        img,
        boxes,
    ) = detector.findFaces(img)

    if boxes:
        box = boxes[0]["bbox"]  # берем первый прямоугольник (x, y, w, h)

        if prev_box is not None:
            (
                x,
                y,
                w,
                h,
            ) = box
            (
                px,
                py,
                pw,
                ph,
            ) = prev_box
            x_delta = x - px > movement
            y_delta = y - py > movement
            w_delta = w - pw > movement
            h_delta = h - ph > movement
            if x_delta or y_delta or w_delta or h_delta:
                cv2.putText(
                    img,
                    "Movement detected",
                    (
                        50,
                        50,
                    ),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (
                        0,
                        0,
                        255,
                    ),
                    2,
                )

        prev_box = box

    cv2.imshow(
        "Head/Face Detection - cvzone",
        img,
    )
    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break
