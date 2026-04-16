import os
import random

import cv2
from cvzone.HandTrackingModule import (
    HandDetector,
)

hand = HandDetector(detectionCon=0.1)
# создания переменную для обнаружения руки
cam = cv2.VideoCapture(0)
cv2.namedWindow("setting")
x1 = 0
y1 = 0
x2 = 0
y2 = 0
SIZE_RECTANGLE = 200


def noth(
    x,
):
    print(x)


cv2.createTrackbar(
    "s1",
    "setting",
    0,
    400,
    noth,
)
cv2.createTrackbar(
    "r",
    "setting",
    0,
    255,
    noth,
)
cv2.createTrackbar(
    "g",
    "setting",
    0,
    255,
    noth,
)
cv2.createTrackbar(
    "b",
    "setting",
    0,
    255,
    noth,
)
cv2.createTrackbar(
    "t",
    "setting",
    1,
    10,
    noth,
)
y4 = 480 - 50
x4 = 0
count = 0

# подключили
imgs = os.listdir("./img")
print(imgs)
randIMG = 0
size = 50
while True:
    img = cv2.imread(f"./img/{imgs[randIMG]}")
    img = cv2.resize(
        img,
        (
            size,
            size,
        ),
    )
    frame = cam.read()[1]
    frame = cv2.flip(
        frame,
        1,
    )
    y3 = 0
    x3 = 0
    (
        hands,
        i,
    ) = hand.findHands(frame)
    p = cv2.getTrackbarPos(
        "s1",
        "setting",
    )
    if hands:
        x1 = hands[0]["lmList"][8][0]
        y1 = hands[0]["lmList"][8][1]
        cv2.circle(
            frame,
            (
                x1,
                y1,
            ),
            10,
            (
                0,
                0,
                0,
            ),
            -1,
        )
    cv2.putText(
        frame,
        str(count),
        (
            x4,
            y4,
        ),
        1,
        2,
        (
            255,
            255,
            255,
        ),
        2,
    )
    frame[
        y4 : y4 + size,
        x4 : x4 + size,
    ] = img
    cv2.imshow(
        "setting",
        frame,
    )

    xState = x4 < x1 < x4 + size
    yState = y4 < y1 < y4 + size
    y4 -= size // 2
    if y4 <= 0:
        x4 = random.randint(
            100,
            400,
        )
        randIMG = random.randint(
            0,
            1,
        )
        size = random.randint(
            10,
            100,
        )
        y4 = 480 - size
    if xState and yState:
        size = random.randint(
            10,
            100,
        )
        randIMG = random.randint(
            0,
            1,
        )
        x4 = random.randint(
            100,
            400,
        )
        count += 1
        y4 = 480 - size

        print("collision")
    cv2.waitKey(1)
