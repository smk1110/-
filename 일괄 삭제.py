import init
while True:
    init.hide_friends()
    init.delete_friends()
    if init.keyboard.is_pressed('s'): #skip
        init.pyautogui.press('backspace')
        while True:
            time_duration = 0.1
            init.time.sleep(time_duration)
            if init.keyboard.is_pressed('s'): #To replay, press 's' again.
                init.pyautogui.press('backspace')
                Delete_OK = init.pyautogui.position()
                break
