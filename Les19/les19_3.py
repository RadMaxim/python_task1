import requests
from data import  bot,types
API_URL = "https://695bbd7e1d8041d5eeb835fd.mockapi.io/api/v1/tokens"
data = requests.get('https://api.binance.com/api/v3/ticker/price').json()

def compare_text(msg, text):
    for elem in data:
        if msg.text == elem["symbol"]:
            bot.reply_to(msg, f"стоимость {msg.text} - {elem['price']}")
            requests.post(API_URL, json={"symbol": elem['symbol'], "price": elem['price']})


@bot.message_handler(commands=['start'])
def start(message):
    # Создаем клавиатуру
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    # Добавляем кнопки
    btn1 = types.KeyboardButton("BTC")
    btn2 = types.KeyboardButton("ETH")
    btn3 = types.KeyboardButton("BNB")
    btn4 = types.KeyboardButton("Другая крипта")

    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(message.chat.id, "Выберите криптовалюту:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "BTC":
        bot.send_message(message.chat.id, "Bitcoin: $45,000")
    elif message.text == "ETH":
        bot.send_message(message.chat.id, "Ethereum: $3,000")
    elif message.text == "Другая крипта":
        bot.send_message(message.chat.id, "Введите тикер вручную:")
@bot.message_handler(content_types=["text"])
def message_handler(msg):
    print(msg.text)
    compare_text(msg, msg.text)


bot.polling()
