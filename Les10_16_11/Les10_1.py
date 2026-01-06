import cv2
import random
from cvzone.HandTrackingModule import HandDetector

hand = HandDetector(detectionCon=0.1)
# создания переменную для обнаружения руки
cam = cv2.VideoCapture(0)
cv2.namedWindow("setting")
x1 = 0
y1 = 0
x2 = 0
y2 = 0
SIZE_RECTANGLE = 200

def noth(x):
    print(x)


cv2.createTrackbar("s1", "setting", 0, 400, noth)
cv2.createTrackbar("r", "setting", 0, 255, noth)
cv2.createTrackbar("g", "setting", 0, 255, noth)
cv2.createTrackbar("b", "setting", 0, 255, noth)
cv2.createTrackbar("t", "setting", 1, 10, noth)
y4 = 0
x4 = 0
count = 0
# подключили
while True:
    frame = cam.read()[1]
    frame = cv2.flip(frame, 1)
    y3 = 0
    x3 = 0
    hands, i = hand.findHands(frame)
    p = cv2.getTrackbarPos("s1", "setting")
    r_color = cv2.getTrackbarPos("r", "setting")
    b_color = cv2.getTrackbarPos("g", "setting")
    g_color = cv2.getTrackbarPos("b", "setting")
    t = cv2.getTrackbarPos("t", "setting")


    if hands:
        x1 = hands[0]['lmList'][4][0]
        y1 = hands[0]['lmList'][4][1]
        x2 = hands[0]['lmList'][8][0]
        y2 = hands[0]['lmList'][8][1]
        cv2.circle(frame, (x1, y1), 10, (0, 0, 0), -1)
        cv2.circle(frame, (x2, y2), 10, (0, 0, 0), -1)
        r = pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5)
        print(r)
        cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 0), 3)
        cv2.putText(frame,str(r), (50,50), 1, 1,(0,0,0),1)
        if r<20:
            print("touch")
            x3 = (x2 + x1) // 2
            y3 = (y2 + y1) // 2
            cv2.rectangle(frame, (x3, y3), (x3 + p, y3 + p), (r_color, b_color, g_color), t)

        else:
            print("not touch")
    cv2.putText(frame, str(count),(x4, y4),1, 2,(255,255,255),2)
    cv2.rectangle(frame, (x4,y4),(x4+50, y4+50),(0,0,0),-1)

    cv2.imshow("setting", frame)
    xState = x4<x3<x4+50
    yState = y4<y3<y4+50
    if xState and yState:
        x4 = random.randint(100,400)
        y4 = random.randint(100,400)
        count+=1

        print("collision")
    cv2.waitKey(1)
