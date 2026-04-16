import time

from data import (
    bot,
    types,
    uno,
)
from service import (
    getAllDataColor,
)


@bot.message_handler(commands=["color"])
def send_inline_keyboard(
    message,
):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn = types.InlineKeyboardButton(
        text="green",
        callback_data="g",
    )
    btn1 = types.InlineKeyboardButton(
        text="red",
        callback_data="r",
    )
    btn2 = types.InlineKeyboardButton(
        text="blue",
        callback_data="b",
    )
    btn3 = types.InlineKeyboardButton(
        text="white",
        callback_data="w",
    )
    btn4 = types.InlineKeyboardButton(
        text="mode1",
        callback_data="m1",
    )
    markup.add(
        btn,
        btn1,
        btn2,
        btn3,
        btn4,
    )
    bot.send_message(
        message.chat.id,
        "Выберите цвет",
        reply_markup=markup,
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(
    call,
):
    if call.data == "m1":
        for c in getAllDataColor():
            uno.write(str(c["color"]).encode())
            time.sleep(int(c["time"]))

    uno.write(str(call.data).encode())


bot.polling()
