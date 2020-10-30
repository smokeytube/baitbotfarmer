#Coded by smokeytube
#NOT IN USE
from datetime import datetime
import pyautogui
import time
from tkinter import mainloop

now = datetime.now()

h = 1
dailytime = ("17")
time.sleep(5)
while h < 2:
    current_time = now.strftime("%H")
    if current_time == dailytime:
        print ("success")
        pyautogui.typewrite("-daily")
        time.sleep(1)
        pyautogui.press('enter')
        pyautogui.typewrite("-buy 19 max")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(86450)
    else:
        time.sleep(1000)
mainloop


