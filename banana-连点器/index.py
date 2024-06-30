import pyautogui
import keyboard
import threading

# Flag to control the clicking loop
clicking = False

def click_mouse():
    global clicking
    while clicking:
        pyautogui.click()
        pyautogui.PAUSE = 0.01  # Adjust the pause to control click speed

def start_stop_clicking():
    global clicking
    if clicking:
        clicking = False
    else:
        clicking = True
        threading.Thread(target=click_mouse).start()

# Set the hotkey to 'ctrl+shift+c' to start/stop clicking
keyboard.add_hotkey('ctrl+shift+c', start_stop_clicking)

print("Press 'ctrl+shift+c' to start/stop clicking.")
keyboard.wait('esc')  # Wait for the 'esc' key to exit the program
print("Program exited.")
