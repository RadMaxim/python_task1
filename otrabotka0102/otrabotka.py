import time

import serial

uno = serial.Serial(
    "COM3",
    9600,
    timeout=0.1,
)
while True:
    val = input("Enter any color: ")
    uno.write(val.encode())
    time.sleep(1)
