#Coded by smokeytube
from tkinter import mainloop
import pyautogui, time, random

time.sleep(5)


h = 1
while h < 2:
    rand = random.randint(1, 5)
    if rand == 1:
        pyautogui.typewrite("-daily")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(86405)
    elif rand == 2:
        pyautogui.typewrite("-daily")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(86500)
    elif rand == 3:
        pyautogui.typewrite("-daily")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(86450)
    elif rand == 4:
        pyautogui.typewrite("-daily")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(86550)
    elif rand == 5:
        pyautogui.typewrite("-daily")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(86490)
    

mainloop
