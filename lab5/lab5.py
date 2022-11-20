import pyautogui
import keyboard
import time


def cautare_google():
    if pyautogui.locateOnScreen(r"C:\Users\MONICA\OneDrive\Desktop\Inteligenta artificiala\lab5.png", confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(
            r"C:\Users\MONICA\OneDrive\Desktop\Inteligenta artificiala\lab5.png", confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(3)
        pyautogui.write("http://youtube.com")
        pyautogui.press('enter')

        time.sleep(2)

    if pyautogui.locateOnScreen(r"C:\Users\MONICA\OneDrive\Desktop\Inteligenta artificiala\yt.png", confidence=0.7) != None:
        camp_YT = pyautogui.locateOnScreen(
            r"C:\Users\MONICA\OneDrive\Desktop\Inteligenta artificiala\yt.png", confidence=0.7)
        pyautogui.click(camp_YT)
        time.sleep(2)
        pyautogui.write("zona it")
        pyautogui.press('enter')

        time.sleep(2)

    if pyautogui.locateOnScreen(r"C:\Users\MONICA\OneDrive\Desktop\Inteligenta artificiala\labsubs.png", confidence=0.7) != None:
        camp_sub = pyautogui.locateOnScreen(
            r"C:\Users\MONICA\OneDrive\Desktop\Inteligenta artificiala\labsubs.png", confidence=0.7)
        pyautogui.click(camp_sub)


time.sleep(2)
cautare_google()
