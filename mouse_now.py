#! python3
# 实时显示当前鼠标指针的坐标
import pyautogui
print('Press Ctrl-C to quit.')
try:
    while True:
        x,y=pyautogui.size()
        outputstr='X:'+str(x).rjust(4)+'Y:'+ str(y).rjust(4)
        print(outputstr, end='')
except KeyboardInterrupt:
    print('\nDone.')