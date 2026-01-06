import telebot, cv2, numpy as np
from data import bot, idBot
from cvzon_helper import detector
from cv2_helper import cam, cv2, cvtColor_helper_hls
# Токен от BotFather
bot = telebot.TeleBot("8300602005:AAG8KBo6LRQCS-YP_mdqM70ZSIYyaNsJI70")

# Обработка входящих сообщений
@bot.message_handler()
def echo_message(message):
    bot.reply_to(message, f"Вы написали: {message.text}")

# Запуск бота

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    print(message.photo[-1])
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    print(file_info)
    downloaded_file = bot.download_file(file_info.file_path)
    # Превращаем байты в numpy-массив
    np_arr = np.frombuffer(downloaded_file, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    # Сохраняем через cv2.imwrite
    cv2.imwrite("images/photo.jpg", img)
    img = cv2.imread("images/photo.jpg")
    res, faces =detector.findFaces(img)
    itog = cv2.imwrite("images/photo_res.jpg", res)
    bot.send_photo(idBot,open("images/photo_res.jpg","rb"),caption=f"{len(faces)}")
    # bot.reply_to(message, "Фото сохранено в папку images ✅")


bot.polling()
