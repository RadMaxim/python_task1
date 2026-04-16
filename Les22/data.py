import serial
import telebot

token = "8508212981:AAEDMqR3JM7JaP1fs0MYliAGzHha1qWCXMs"
idBot = 563747470
bot = telebot.TeleBot(token=token)

port = "COM3"
uno = serial.Serial(
    port,
    9600,
    timeout=0.1,
)
