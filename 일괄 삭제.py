import init
while True:
    init.hide_friends()
    init.delete_friends()
    if init.keyboard.is_pressed('s'): #skip
        init.pyautogui.press('backspace')
        init.pause('s')