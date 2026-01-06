import telebot,cv2

bot = telebot.TeleBot("8508212981:AAEDMqR3JM7JaP1fs0MYliAGzHha1qWCXMs")
bot_id = 563747470
while True:
    bot.send_message(bot_id, "hello")
    cv2.waitKey(1000)
