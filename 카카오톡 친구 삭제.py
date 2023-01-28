import init

while True:    
    if init.keyboard.is_pressed('h'):
        init.pyautogui.press('backspace')
        init.hide_friends()
    if init.keyboard.is_pressed('j'):
        init.pyautogui.press('backspace')
        for i in range(7):
            init.hide_friends()

    if init.keyboard.is_pressed('d'):
        init.pyautogui.press('backspace')
        init.delete_friends()
    if init.keyboard.is_pressed('f'):
        init.pyautogui.press('backspace')
        for k in range(10):
            init.delete_friends()
    
    if init.keyboard.is_pressed('q'):
        init.pyautogui.press('backspace')
        init.hide_friends()
        init.delete_friends()
    if init.keyboard.is_pressed('w'):
        init.pyautogui.press('backspace')
        for i in range(7):
            init.hide_friends()
            init.delete_friends()
    if init.keyboard.is_pressed('s'):
        init.pyautogui.press('backspace')
        init.skip_friends()

        
        




