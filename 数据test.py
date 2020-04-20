import pyautogui
import time



pyautogui.moveTo(180,440)
pyautogui.mouseDown()
pyautogui.dragTo(250,460,duration=5)
pyautogui.mouseUp(250,460)
pyautogui.hotkey('ctrl','c')