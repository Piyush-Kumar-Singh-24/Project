import pyautogui
import time

time.sleep(2)
text = "Happy Birthday To You harami"

for i in range(10):
    pyautogui.typewrite(text)
    pyautogui.press('enter')