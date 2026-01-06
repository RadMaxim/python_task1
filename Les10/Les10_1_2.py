import cv2
from cvzone.HandTrackingModule import HandDetector
import random
hand = HandDetector(detectionCon=0.1)
# создания переменную для обнаружения руки
cam = cv2.VideoCapture(0)
cv2.namedWindow("setting")
x1 ,y1 ,x2,y2,y3,x3 = 0,0,0,0,0,0
x4, y4 = 100,100
search_size = 50
SIZE_RECTANGLE = 200

def noth(x):
    print(x)
cv2.createTrackbar("s1", "setting", 0, 20, noth)
# подключили
while True:
    frame = cam.read()[1]
    hands, i = hand.findHands(frame)
    p = cv2.getTrackbarPos("s1", "setting")

    if hands:
        x1 = hands[0]['lmList'][4][0]
        y1 = hands[0]['lmList'][4][1]
        x2 = hands[0]['lmList'][8][0]
        y2 = hands[0]['lmList'][8][1]
        cv2.circle(frame, (x1, y1), 10, (0, 0, 0), -1)
        cv2.circle(frame, (x2, y2), 10, (0, 0, 0), -1)
        r = pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5)
        cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 0), 3)
        cv2.putText(frame,str(r), (50,50), 1, 1,(0,0,0),1)
        if r<20:
            print("touch")
            x3 = (x2 + x1) // 2
            y3 = (y2 + y1) // 2


        else:
            print("not touch")
    if x3<x4-search_size//2 and x4+search_size//2<x3 + SIZE_RECTANGLE and y3<y4-search_size//2 and y4+search_size//2<y3 + SIZE_RECTANGLE:
        x4 = random.randint(100,400)
        y4 = random.randint(100,400)

    cv2.rectangle(frame, (x3, y3), (x3 + SIZE_RECTANGLE, y3 + SIZE_RECTANGLE), (0, 0, 0), 2)
    cv2.rectangle(frame, (x4-search_size//2, y4-search_size//2),(x4+search_size//2, y4+search_size//2),(0,0,0),-1)
    cv2.imshow("setting", frame)
    cv2.waitKey(1)
