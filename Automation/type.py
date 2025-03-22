import pyautogui
import time

def auto_write(text):
    text = text.replace("search", "")
    text = text.replace("type", "")
    text = text.strip()
    #print("Please focus on the input field. Writing will start in 3 seconds...")
    #time.sleep(3)  # Aapko time mile input field par focus karne ke liye
    pyautogui.write(text)  # Har character ke beech ka delay (smooth typing effect)



