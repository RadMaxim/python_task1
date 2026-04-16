import cv2
from cvzone.FaceDetectionModule import (
    FaceDetector,
)
from cvzone.HandTrackingModule import (
    HandDetector,
)

cam = cv2.VideoCapture(0)
count = 0
hand = HandDetector(detectionCon=0.8)
detector = FaceDetector(minDetectionCon=0.7)
pointHand = 0


def comparePointHand():
    global pointHand
    if pointHand > 21:
        pointHand = 0


def drawPonts(
    hands,
    frame,
):
    global pointHand
    pointHand += 1
    if hands:
        for (
            id,
            point,
        ) in enumerate(
            hands[0]["lmList"],
            0,
        ):
            (
                x,
                y,
                _,
            ) = point
            if pointHand == id:
                cv2.circle(
                    frame,
                    (
                        x,
                        y,
                    ),
                    5,
                    (
                        0,
                        0,
                        0,
                    ),
                    -1,
                )


def cvtFrame(
    frame,
):
    frame = cv2.flip(
        frame,
        1,
    )
    return frame


def cvtHSV(
    frame,
):
    res = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2HSV,
    )
    return res


while True:
    frame = cam.read()[1]
    frame = cvtFrame(frame)
    (
        img,
        faces,
    ) = detector.findFaces(
        frame,
        draw=True,
    )
    (
        h,
        _,
    ) = hand.findHands(frame)
    print(h)
    drawPonts(
        h,
        frame,
    )
    comparePointHand()
    hsv = cvtHSV(frame)
    cv2.imshow(
        "hsv",
        hsv,
    )
    cv2.imshow(
        "frame",
        frame,
    )
    cv2.waitKey(1)
    count += 1
    if count > pow(
        10,
        9,
    ):
        break
