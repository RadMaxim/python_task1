import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
from token_id import idBot, cam, bot

detector = FaceMeshDetector(maxFaces=15)

prev_frame_x = 0
prev_frame_y = 0
while True:
    frame = cam.read()[1]
    img, faces = detector.findFaceMesh(frame)
    print(faces)
    if len(faces) > 0:
        x = faces[0][0][0]
        y = faces[0][0][1]
        if abs(x-prev_frame_x)>10 or abs(prev_frame_y-y)>10:

            cv2.imwrite(f"./../imgForBot/frame_detect.jpg", frame)

            bot.send_photo(idBot,
                           open(f"./../imgForBot/frame_detect.jpg", "rb"),
                           caption="Обнаружение человека")
            cv2.waitKey(1000)
    cv2.imshow("frame", frame)
    cv2.waitKey(1)
    if len(faces)>0:
        prev_frame_x = faces[0][0][0]
        prev_frame_y = faces[0][0][1]
