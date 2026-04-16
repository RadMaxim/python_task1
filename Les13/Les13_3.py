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
        for (
            id,
            point,
        ) in enumerate(face):
            (
                x,
                y,
            ) = point
            cv2.circle(
                img,
                (
                    x,
                    y,
                ),
                2,
                (
                    0,
                    255,
                    0,
                ),
                -1,
            )  # рисуем точки
            if id % 10 == 0:
                cv2.putText(
                    img,
                    str(id),
                    (
                        x,
                        y,
                    ),
                    1,
                    1,
                    (
                        0,
                        0,
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
