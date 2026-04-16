import cv2
from cvzone.HandTrackingModule import (
    HandDetector,
)

hand = HandDetector(detectionCon=0.1)
cam = cv2.VideoCapture(0)


while True:
    frame = cam.read()[1]
    frame = cv2.flip(
        frame,
        1,
    )
    (
        hands,
        i,
    ) = hand.findHands(frame)

    if len(hands) == 2:
        x1 = hands[0]["lmList"][4][0]
        y1 = hands[0]["lmList"][4][1]
        x2 = hands[0]["lmList"][8][0]
        y2 = hands[0]["lmList"][8][1]
        x3 = hands[1]["lmList"][4][0]
        y3 = hands[1]["lmList"][4][1]
        x4 = hands[1]["lmList"][8][0]
        y4 = hands[1]["lmList"][8][1]
        cv2.rectangle(
            frame,
            (
                x2,
                y2,
            ),
            (
                x3,
                y3,
            ),
            (
                0,
                0,
                0,
            ),
            -1,
        )
    cv2.imshow(
        "frame",
        frame,
    )
    cv2.waitKey(1)
