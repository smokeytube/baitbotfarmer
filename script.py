#Coded by smokeytube
from tkinter import mainloop
import pyautogui, time, random

time.sleep(5)


h = 1
while h < 2:
    rand = random.randint(1, 5)
    if rand == 1:
        pyautogui.typewrite("-work")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(303)
    elif rand == 2:
        pyautogui.typewrite("-work")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(310)
    elif rand == 3:
        pyautogui.typewrite("-work")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(362)
    elif rand == 4:
        pyautogui.typewrite("-work")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(308)
    elif rand == 5:
        pyautogui.typewrite("-work")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(333)
    

mainloop
