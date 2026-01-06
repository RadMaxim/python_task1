import cv2
from cvzone.HandTrackingModule import HandDetector
hand = HandDetector(detectionCon=0.1)
#создания переменную для обнаружения руки
cam = cv2.VideoCapture(0)
#подключили
while True:
    frame = cam.read()[1]
    h,i =hand.findHands(frame)
    cv2.imshow("my_hand", frame)
    cv2.waitKey(1)
