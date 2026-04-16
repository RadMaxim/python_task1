from data import (
    bot,
    idBot,
    types,
    uno,
)

print(67)


@bot.message_handler(commands=["start"])
def handler_start(
    msg,
):
    keybord = types.InlineKeyboardMarkup(row_width=3)
    btn1 = types.InlineKeyboardButton(
        text="red",
        callback_data="r",
    )
    btn2 = types.InlineKeyboardButton(
        text="blue",
        callback_data="b",
    )
    btn3 = types.InlineKeyboardButton(
        text="gey",
        callback_data="g",
    )
    btn4 = types.InlineKeyboardButton(
        text="mode",
        callback_data="m",
    )
    keybord.add(
        btn1,
        btn2,
        btn3,
        btn4,
    )
    bot.send_message(
        idBot,
        "Show buton",
        reply_markup=keybord,
    )


@bot.callback_query_handler(func=lambda call: True)
def callbackBTN(
    call,
):
    uno.write(f"{call.data}".encode())
    print(call.data)


bot.polling()
