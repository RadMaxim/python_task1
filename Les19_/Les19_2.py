from data import (
    bot,
    idBot,
)
from Les19_1 import (
    getTokenFromBinance,
)

bot.send_message(
    idBot,
    "Maxim",
)


@bot.message_handler(content_types="text")
def getTokenPriceFromBinance(
    msg,
):
    text = msg.text
    print(msg)
    resp = getTokenFromBinance(text)
    bot.reply_to(
        msg,
        str(resp),
    )


bot.polling()
