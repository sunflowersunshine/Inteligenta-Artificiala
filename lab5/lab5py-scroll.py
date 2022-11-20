import pyautogui
import keyboard
import time


def cautare_google():
    if pyautogui.locateOnScreen(r"C:\Users\MONICA\OneDrive\Desktop\Inteligenta artificiala\lab5.png", confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(
            r"C:\Users\MONICA\OneDrive\Desktop\Inteligenta artificiala\lab5.png", confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(3)
        pyautogui.write("https://www.youtube.com/c/ZonaitTvro/videos")
        pyautogui.press('enter')

        time.sleep(2)

        pyautogui.scroll(-100)


def coordonate():
    print(pyautogui.position())


def scrollDown():
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')


def back():
    if pyautogui.locateOnScreen(r"C:\Users\MONICA\OneDrive\Desktop\Inteligenta artificiala\back.png", confidence=0.7) != None:
        camp_back = pyautogui.locateOnScreen(
            r"C:\Users\MONICA\OneDrive\Desktop\Inteligenta artificiala\back.png", confidence=0.7)
        pyautogui.click(camp_back)


time.sleep(2)
cautare_google()


# while not keyboard.is_pressed('esc'):
#     coordonate()

clicked = 0
x = 1220
y = 389

while not keyboard.is_pressed('esc'):

    time.sleep(2)

    scrollDown()

    time.sleep(2)

    pyautogui.click(x, y)

    time.sleep(10)

    back()

    time.sleep(2)

    pyautogui.click(x + 300, y)

    time.sleep(10)

    back()

    time.sleep(2)
