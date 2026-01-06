import random, os, cvzone,telebot, cv2
from cvzone.FaceMeshModule import FaceMeshDetector

detector = FaceMeshDetector(maxFaces=15)


cam = cv2.VideoCapture(0)
token = ""
idBot = 0000000
bot = telebot.TeleBot(token=token)

while True:
    frame = cam.read()[1]
    img, faces = detector.findFaceMesh(frame)
    imgs = os.listdir("./../imgForBot")
    print(imgs)
    lastIndex = len(imgs)-1
    rand = random.randint(0,100)
    cv2.imwrite(f"./../imgForBot/frame{rand}.jpg",frame)
    bot.send_photo(idBot,
                   open(f"./../imgForBot/{imgs[lastIndex]}","rb"),
                   caption="Обнаружение человека")
    cv2.imshow("frame", frame)
    cv2.waitKey(1000)
