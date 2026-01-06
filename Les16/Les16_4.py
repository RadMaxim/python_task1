import cv2
from cvzone.FaceDetectionModule import FaceDetector
from token_id import idBot, cam, bot

detector = FaceDetector(minDetectionCon=0.7)  # порог уверенности

prev_frame_x = 0
prev_frame_y = 0
while True:
    frame = cam.read()[1]
    img, faces = detector.findFaces(frame, draw=True)

    if len(faces) > 0:
        x = faces[0]["bbox"][0]
        y = faces[0]["bbox"][1]
        if abs(x-prev_frame_x)>10 or abs(prev_frame_y-y)>10:

            if len(faces)==1:
                face_1 = frame[faces[0]["bbox"][1]:faces[0]["bbox"][1]+faces[0]["bbox"][3], faces[0]["bbox"][0]:faces[0]["bbox"][0]+faces[0]["bbox"][2]]
                cv2.imwrite(f"./../imgForBot/frame_1.jpg", face_1)

                bot.send_photo(idBot,
                               open(f"./../imgForBot/frame_1.jpg", "rb"),
                               caption="Обнаружение человека")
            cv2.waitKey(1000)
    cv2.imshow("frame", frame)
    cv2.waitKey(1)
    if len(faces)>0:
        prev_frame_x = faces[0]["bbox"][0]
        prev_frame_y = faces[0]["bbox"][1]
