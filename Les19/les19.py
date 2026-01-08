from Les19_1_1 import getAllDataFromBinance, getSymbolDataFromBinance
from data import  bot

def compare_text(msg):
    res = getSymbolDataFromBinance(msg.text)
    if res:
        bot.reply_to(msg, f'стоимость {res["symbol"]} - {res["price"]}')

@bot.message_handler(commands=['start'])
def handle_start(msg):
    bot.send_message(msg.chat.id, "Добро пожаловать! 🎉")
@bot.message_handler(commands=['price'])
def handle_start(msg):
    res1 = getAllDataFromBinance()[:3]
    bot.send_message(msg.chat.id, f"{res1}")

@bot.message_handler(content_types=["text"])
def message_handler(msg):
    compare_text(msg)


bot.polling()
