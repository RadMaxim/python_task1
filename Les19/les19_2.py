import requests
from data import  bot
API_URL = "https://695bbd7e1d8041d5eeb835fd.mockapi.io/api/v1/tokens"
data = requests.get('https://api.binance.com/api/v3/ticker/price').json()

def compare_text(msg, text):
    for elem in data:
        if msg.text == elem["symbol"]:
            bot.reply_to(msg, f"стоимость {msg.text} - {elem['price']}")
            requests.post(API_URL, json={"symbol": elem['symbol'], "price": elem['price']})


@bot.message_handler(content_types=["text"])
def message_handler(msg):
    print(msg.text)
    compare_text(msg, msg.text)


bot.polling()
