import pyautogui
import time

pyautogui.FAILSAFE = True

print("Click inside Notepad within 5 seconds...")
time.sleep(5)

pyautogui.write("Hello from Gesture Controller!", interval=0.05)

print("Typing completed!")