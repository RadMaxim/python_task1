import requests
from data import idBot, bot

data = requests.get('https://api.binance.com/api/v3/ticker/price').json()

def compare_text(msg, text):
    for elem in data:
        if msg.text == elem["symbol"]:
            bot.reply_to(msg, f"стоимость {msg.text} - {elem['price']}")


@bot.message_handler(content_types=["text"])
def message_handler(msg):
    print(msg.text)
    compare_text(msg, msg.text)


bot.polling()
