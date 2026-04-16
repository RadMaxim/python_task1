import random
import time

import cv2
from cvzone.PoseModule import (
    PoseDetector,
)
from saveDataMockApi import (
    saveData,
)
from saveInfoCSV import (
    addData,
    createCSV,
)

createCSV()
detector = PoseDetector()
cap = cv2.VideoCapture(0)
start_time = time.time()

while True:
    (
        ret,
        frame,
    ) = cap.read()
    if not ret:
        break

    # Обнаружение позы
    frame = detector.findPose(
        frame,
        draw=True,
    )
    (
        lmList,
        bbox,
    ) = detector.findPosition(
        frame,
        draw=False,
    )
    if len(lmList):
        if len(lmList) > 25:
            right_knee = lmList[25]  # [id, x, y, confidence]
            print(f"Правое колено: x={right_knee[1]}, y={right_knee[2]}")

            # Координаты левой лодыжки (точка 28)
        if len(lmList) > 28:
            left_ankle = lmList[28]
            print(f"Левая лодыжка: x={left_ankle[1]}, y={left_ankle[2]}")

        current_time = time.time()
        different = current_time - start_time
        rating = random.randint(
            1,
            4,
        )
        print("сохраняем в двух местах, в csv и mockapi")
        saveData(
            different,
            rating,
        )
        addData(
            str(different),
            rating,
        )
        start_time = current_time
    cv2.imshow(
        "Squat Counter",
        frame,
    )
    if time.time() - start_time > 60:
        print("send data")

    # Выход по нажатию 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
