if (__name__ == "__main__"):
    print("Don't open on the main file.")
    exit()
try:
    import pyautogui
    import keyboard
    import time
    import pickle
except ModuleNotFoundError:
    print("You have not installed some modules.")
    print("Please install pyautogui, keyboard, pickle with pip.")
    exit()
print("Do you have an data.pickle file saved before?")
while True:
    
    a = input("[R] I want to reset. / [I] Yes, Import it. : ")
    if a in ["I", "i"]:
        with open ("data.pickle", 'rb') as p:
            position = pickle.load(p)
        (Friend, Hide, Delete, Block)= position
        break

    elif a in ["R", "r"]:

        print("Press 's' on the top of your friend profiles.")
        while True:
            time_duration = 0.1
            time.sleep(time_duration)
            if keyboard.is_pressed('s'):
                pyautogui.press('backspace')
                Friend = pyautogui.position()
                break
        pyautogui.moveTo(Friend) #카톡 친구 위치로 이동
        pyautogui.click(button='right')
        Hide = (Friend.x+30, Friend.y +200)
        pyautogui.moveTo(Hide)
        pyautogui.click(button='left')
        print("Press 's' on 'Delete' (Settings/Friends/Hidden Friends)")
        while True:
            time_duration = 0.1
            time.sleep(time_duration)
            if keyboard.is_pressed('s'):
                pyautogui.press('backspace')
                Delete = pyautogui.position()
                break
        Block = (Friend.x+30, Friend.y +230)

        data = (Friend, Hide, Delete, Block)
        with open('data.pickle', 'wb') as f:
            pickle.dump(data, f)
        break
    else:
        print("Please enter a valid input.")

print("The top of your friend profiles : ("+str(Friend.x)+",", str(Friend.y)+")")
print("Hide button : "+str(Hide))
print("Delete button : ("+str(Delete.x)+",", str(Delete.y)+")")
print("Block button : "+str(Block))

print("Now all set!")

def hide_friends():
    
    pyautogui.moveTo(Friend) #카톡 친구 위치로 이동
    pyautogui.click(button='right')
    pyautogui.moveTo(Hide) #숨김
    pyautogui.click(button='left')
def delete_friends():
    
    pyautogui.moveTo(Delete)
    pyautogui.click(button='left')
    pyautogui.press('space')
    pyautogui.click(button='left')

def skip_friends():
    
    pyautogui.moveTo(Friend) #차단
    pyautogui.click(button='right')
    pyautogui.moveTo(Block)
    pyautogui.click(button='left')
    pyautogui.press('space')
    pyautogui.click(button='left')