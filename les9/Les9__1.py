import cv2
from cvzone.HandTrackingModule import (
    HandDetector,
)

hand = HandDetector(detectionCon=0.1)
# создания переменную для обнаружения руки
cam = cv2.VideoCapture(0)
cv2.namedWindow("setting")


def noth(
    x,
):
    print(x)


cv2.createTrackbar(
    "s1",
    "setting",
    0,
    20,
    noth,
)
# подключили
while True:
    frame = cam.read()[1]
    (
        hands,
        i,
    ) = hand.findHands(frame)
    p = cv2.getTrackbarPos(
        "s1",
        "setting",
    )
    print(p)
    if hands:
        x = hands[0]["lmList"][p][0]
        y = hands[0]["lmList"][p][1]
        cv2.circle(
            frame,
            (
                x,
                y,
            ),
            10,
            (
                0,
                0,
                0,
            ),
            -1,
        )

    cv2.imshow(
        "setting",
        frame,
    )
    cv2.waitKey(1)
