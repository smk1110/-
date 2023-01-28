import pyautogui
import keyboard


def hide_friends():
    
    pyautogui.moveTo(x=1711, y=149) #카톡 친구 위치로 이동
    pyautogui.click(button='right')
    pyautogui.moveTo(x=1728, y=345) #삭제
    pyautogui.click(button='left')
def delete_friends():
    
    pyautogui.moveTo(x=1458, y=364)
    pyautogui.click(button='left')
    pyautogui.moveTo(x=1169, y=357)
    pyautogui.click(button='left')

def skip_friends():
    
    pyautogui.moveTo(x=1711, y=149) #차단
    pyautogui.click(button='right')
    pyautogui.moveTo(x=1721, y=366)
    pyautogui.click(button='left')
    pyautogui.moveTo(x=1619, y=390)
    pyautogui.click(button='left')