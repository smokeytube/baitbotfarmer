#Coded by smokeytube
#Expiremental. Will do -daily everyday at 12
#(Works best for 24 hour clocks, will do -daily twice with 12 hour clocks)
from datetime import datetime
import pyautogui, time, random

time.sleep(5)

now = datetime.now()

dailytime = ("12")
current_time = now.strftime("%H")

while True:
    rand = random.randint(305, 350)
    if current_time == dailytime:
        pyautogui.typewrite("-daily")
        time.sleep(1)
        pyautogui.press('enter')
        pyautogui.typewrite("-buy 19 max")
        time.sleep(1)
        pyautogui.press('enter')
    elif True:
        pyautogui.typewrite("-work")
        time.sleep(1)
        pyautogui.press('enter')
        pyautogui.typewrite("-buy 19 max")
        time.sleep(1)
        pyautogui.press('enter')
    time.sleep(rand)


