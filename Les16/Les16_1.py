import random, os, cv2
from cvzone.FaceMeshModule import FaceMeshDetector
from token_id import  idBot, cam, bot
detector = FaceMeshDetector(maxFaces=15)


while True:
    frame = cam.read()[1]
    img, faces = detector.findFaceMesh(frame)
    imgs = os.listdir("./../imgForBot")
    lastIndex = len(imgs)-1
    rand = random.randint(0,100)
    cv2.imwrite(f"./../imgForBot/frame{rand}.jpg",frame)
    bot.send_photo(idBot,
                   open(f"./../imgForBot/{imgs[lastIndex]}","rb"),
                   caption="Обнаружение человека")
    cv2.imshow("frame", frame)
    cv2.waitKey(1000)
