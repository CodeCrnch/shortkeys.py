import keyboard
import time

keyboard.add_hotkey('ctrl+1', lambda: keyboard.write(
    "Dont forget to "))
keyboard.add_hotkey('ctrl+2', lambda: keyboard.write(
    "like and follow!"))

while True:
    time.sleep(0.1)