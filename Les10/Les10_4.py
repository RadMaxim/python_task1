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

y3 = 200
x3 = 200
cx = 0
cy = 0
r=0
cv2.createTrackbar("s1", "setting", 0, 20, noth)
count = 0
# подключили
while True:

    img = cv2.imread("./img/pngtree-trash-can-png-image_4339902.png")

    frame = cam.read()[1]
    frame = cv2.flip(frame, 1)

    hands, i = hand.findHands(frame)
    p = cv2.getTrackbarPos("s1", "setting")
    print(p)
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
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2

        if r < 20 and x3 - SIZE_RECTANGLE // 2 < cx < x3 + SIZE_RECTANGLE // 2 and y3 - SIZE_RECTANGLE // 2 < cy < y3 + SIZE_RECTANGLE // 2:
            print("touch")
            x3 = cx
            y3 = cy


        else:
            print("not touch")
    cv2.rectangle(frame, (x3-SIZE_RECTANGLE//2, y3-SIZE_RECTANGLE//2), (x3 + SIZE_RECTANGLE//2, y3 + SIZE_RECTANGLE//2), (0, 0, 0), 2)
    img = cv2.resize(img, (100, 100))
    if 0<cx<100 and 0<cy<100 and r>20 and x3 - SIZE_RECTANGLE // 2 < cx < x3 + SIZE_RECTANGLE // 2 and y3 - SIZE_RECTANGLE // 2 < cy < y3 + SIZE_RECTANGLE // 2:
        x3  = random.randint(0,640)
        y3  = random.randint(0,480)
        count+=1




    frame[0:100, 0:100] = img
    cv2.putText(frame, str(count),(50,50),1,2,(255,255,255),3)

    cv2.imshow("setting", frame)
    cv2.waitKey(1)
