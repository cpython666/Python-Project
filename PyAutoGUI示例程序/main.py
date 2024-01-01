a1=(895,915)
a2=(1116,853)
a3=(1593,223)
import pyautogui
import time
# 左键长按两秒
def long_press():
    pyautogui.mouseDown()
    time.sleep(2.5)
    pyautogui.mouseUp()
# 循环执行动作
while True:
    pyautogui.moveTo(a1)
    long_press()
    pyautogui.doubleClick(a2)
    time.sleep(0.5)
    pyautogui.click(a3)
    time.sleep(0.5)
    pyautogui.click(a3)
    time.sleep(0.5)
    pyautogui.click(a3)
    time.sleep(0.5)