from data import (
    bot,
    idBot,
)

bot.send_message(
    idBot,
    "hello Maxim",
)


def compare_text(
    msg,
    text,
):
    if text == "git init":
        bot.reply_to(
            msg,
            "для инициализации гита",
        )
    elif text == "git add .":
        bot.reply_to(
            msg,
            "Для добавления в индексацию",
        )
    elif text == "git commit":
        bot.reply_to(
            msg,
            "внесли коммит",
        )


@bot.message_handler(content_types=["text"])
def message_handler(
    msg,
):
    print(msg.text)
    compare_text(
        msg,
        msg.text,
    )


bot.polling()
