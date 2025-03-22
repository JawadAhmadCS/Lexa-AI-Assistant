import random
import pyautogui

from my.head.Speak import speak
from my.Data.dlg import res_bye, bye_key_word, websites
from my.head.processing import process
from my.Automation.websearch import browse
from my.Data.dlg import apps
from my.Modules.openapp import openapp
from my.Automation.type import auto_write

def recognize(user_input):
    try:
        # Exit on bye keywords
        if user_input in bye_key_word:
            goodbye_message = random.choice(res_bye)
            print(goodbye_message)
            speak(goodbye_message)
            exit()

        # Clean and process input
        new_user_input = user_input.replace("open", "").strip()

        # Open Apps

        if new_user_input in apps:
            print(f"Just a second, opening {new_user_input}")
            speak(f"Just a second, opening {new_user_input}")
            result = openapp(new_user_input)
            print(result)
            speak(result)
            return  # Exit function after handling app open

        # Open Websites

        elif new_user_input in websites:
            print(f"Just a second, opening {new_user_input}")
            speak(f"Just a second, opening {new_user_input}")
            result = browse(new_user_input)
            print(result)
            speak(result)
            return  # Exit function after handling website

        # Search and auto-write functionality
        if user_input.startswith("search"):
            auto_write(user_input)
            pyautogui.press("enter")
            return

        if user_input.startswith("type"):
            auto_write(user_input)
            return
        # Process other inputs
        input_result = process(user_input)
        print(input_result)
        speak(input_result)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        speak("Sorry, something went wrong!")

