from data import (
    uno,
)

while True:
    val = input("Enter:")
    uno.write(val.encode("utf-8"))

# @bot.message_handler(commands=['color'])
# def send_inline_keyboard(message):
#     markup = types.InlineKeyboardMarkup(row_width=2)
#     btn = types.InlineKeyboardButton(text="green", callback_data=f"g")
#     btn1 = types.InlineKeyboardButton(text="red", callback_data=f"r")
#     btn2 = types.InlineKeyboardButton(text="blue", callback_data=f"b")
#     btn3 = types.InlineKeyboardButton(text="white", callback_data=f"w")
#     markup.add(btn, btn1, btn2, btn3)
#     bot.send_message(message.chat.id, "Выберите цвет", reply_markup=markup)
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     print(call.data)
#     uno.write(str(call.data).encode())
# bot.polling()
