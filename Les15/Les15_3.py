import cv2
import telebot
from cvzone.FaceDetectionModule import (
    FaceDetector,
)

cam = cv2.VideoCapture(0)
bot = telebot.TeleBot("8508212981:AAEDMqR3JM7JaP1fs0MYliAGzHha1qWCXMs")
bot_id = 563747470
detector = FaceDetector(minDetectionCon=0.7)
(
    prevX,
    prevY,
) = (
    0,
    0,
)
count = 0
while True:
    (
        success,
        frame,
    ) = cam.read()
    (
        img,
        boxes,
    ) = detector.findFaces(frame)
    (
        currentX,
        currentY,
    ) = boxes[0]["center"]
    if abs(currentX - prevX) > 2 or abs(currentY - prevY) > 2:
        print("move")
        if len(boxes) > 0:
            count += 1
            bot.send_message(
                bot_id,
                f"hello-{count}",
            )
            cv2.waitKey(1000)
    cv2.imshow(
        "frame",
        frame,
    )
    cv2.waitKey(1)
    prevX = currentX
    prevY = currentY
