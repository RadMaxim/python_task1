import telebot, cv2, numpy as np
from data import bot, idBot
from cvzon_helper import detector
from cv2_helper import cam, cv2, cvtColor_helper_hls
def detector_face(img):
    img_new, faces = detector.findFaces(img)
    print(len(faces))
    cv2.imwrite("./img/result.jpg", img_new)
    bot.send_photo(idBot,
                   open(f"./img/result.jpg", "rb"),caption="smth")
                 


@bot.message_handler(content_types=["photo"])
def message_handler(msg):
    photo = msg.photo[-1].file_id
    file_info = bot.get_file(photo)
    download_file = bot.download_file(file_info.file_path)
    np_arr = np.frombuffer(download_file, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    cv2.imwrite("./img/test.jpg", img)
    save_img = cv2.imread("./img/test.jpg")
    detector_face(save_img)
bot.polling()