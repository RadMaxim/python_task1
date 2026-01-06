import cv2
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)  # можно увеличить число лиц
count = 0
while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=True)

    if faces:
        face = faces[0]
        for id, point in enumerate(face):
            x, y = point
            res = round(count)
            if res==id:
                cv2.circle(img, (x, y), 10, (255, 0, 0), -1)
                cv2.putText(img,str(id),(x,y),1,1,(0,0,0),1)
    cv2.imshow("Face Mesh Detection", img)
    count+=0.1
    cv2.waitKey(1)
