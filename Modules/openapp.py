import pyautogui as ui
import time

def openapp(text):
    try:
        text = text.replace("open", "")
        text = text.strip()
        ui.press("win")
        time.sleep(0.5)
        ui.write(text)
        time.sleep(0.5)
        ui.press("enter")
        return ("Done! " + text + "  is now open for you")

    except Exception as e:
        return f"\rAn error occurred: {e}"



#open("calender")
