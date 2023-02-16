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
def pause(key):
    while True:
        time_duration = 0.1
        time.sleep(time_duration)
        if keyboard.is_pressed(key):
            pyautogui.press('backspace')
            break
print("전에 저장해둔 data.pickle 파일이 있나요?")
while True:
    
    a = input("[R] 그냥 재설정할게요. / [I] 네, 불러와주세요. : ")
    if a in ["I", "i"]:
        with open ("data.pickle", 'rb') as p:
            position = pickle.load(p)
        (Friend, Hide, Delete, Block)= position
        break

    elif a in ["R", "r"]:

        print("친구 목록 가장 위에서 's'를 누르세요.")
        pause('s')
        Friend = pyautogui.position()
        pyautogui.moveTo(Friend) #카톡 친구 위치로 이동
        pyautogui.click(button='right')
        Hide = (Friend.x+30, Friend.y +200)
        pyautogui.moveTo(Hide)
        pyautogui.click(button='left')
        print("'Delete' (Settings/Friends/Hidden Friends)에서 's'를 누르세요.")
        pause('s')
        Delete = pyautogui.position()
        Block = (Friend.x+30, Friend.y +230)

        data = (Friend, Hide, Delete, Block)
        with open('data.pickle', 'wb') as f:
            pickle.dump(data, f)
        break
    else:
        print("정상적인 값이 아닙니다.")

print("친구 목록 최상단 : ("+str(Friend.x)+",", str(Friend.y)+")")
print("숨김 버튼 : "+str(Hide))
print("삭제 버튼 : ("+str(Delete.x)+",", str(Delete.y)+")")
print("차단 버튼 : "+str(Block))

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