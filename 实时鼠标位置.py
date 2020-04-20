import pyautogui
import time

try:
    while True:
        #time.sleep(1)
        x,y=pyautogui.position()
        position='X:'+str(x).rjust(4)+''+'Y:'+str(y).rjust(4)
        print(position,end='')
        print('\b'*len(position),end='',flush=True)
except KeyboardInterrupt:
    print('bye!\n')

