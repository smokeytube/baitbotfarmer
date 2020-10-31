#Coded by smokeytube
import pyautogui, time, random

time.sleep(5)

while True:
    rand = random.randint(86450, 86650)
    pyautogui.typewrite("-daily")
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.typewrite("-buy 19 max")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(rand)
