import pyautogui
import time

print("You have 5 seconds...")
time.sleep(5)

pyautogui.moveRel(200, 0, duration=1)

print("Done!")