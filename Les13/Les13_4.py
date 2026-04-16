import math

import cv2
from cvzone.FaceMeshModule import (
    FaceMeshDetector,
)

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)  # можно увеличить число лиц

while True:
    (
        success,
        img,
    ) = cap.read()
    if not success:
        break

    (
        img,
        faces,
    ) = detector.findFaceMesh(
        img,
        draw=True,
    )  # draw=True рисует все точки

    if faces:
        # faces — список лиц, каждое лицо содержит список координат точек
        face = faces[0]  # берём первое лицо
        top_lip = face[13]  # верхняя губа (центр)
        bottom_lip = face[14]
        cv2.circle(
            img,
            top_lip,
            4,
            (
                255,
                0,
                0,
            ),
            -1,
        )
        cv2.circle(
            img,
            bottom_lip,
            4,
            (
                255,
                0,
                0,
            ),
            -1,
        )
        cv2.line(
            img,
            top_lip,
            bottom_lip,
            (
                255,
                0,
                0,
            ),
            3,
        )
        distance = math.dist(
            top_lip,
            bottom_lip,
        )
        cv2.putText(
            img,
            f"Dist: {int(distance)}",
            (
                top_lip[0],
                top_lip[1] - 20,
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (
                0,
                255,
                0,
            ),
            2,
        )
    cv2.imshow(
        "Face Mesh Detection",
        img,
    )
    if cv2.waitKey(1) & 0xFF == 27:  # ESC для выхода
        break

cap.release()
cv2.destroyAllWindows()
