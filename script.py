#Coded by smokeytube
import pyautogui, time, random

time.sleep(5)

while True:
    rand = random.randint(305, 350)
    pyautogui.typewrite("-work")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(rand)
