import time
import requests
from my.head.Speak import speak
def check_internet():
    try:
        # Google server ko ping karna
        requests.get("http://www.google.com", timeout=3)
        return True
    except requests.ConnectionError:
        return False

def monitor_connection():
    previous_status = None  # Pichla status track karne ke liye

    while True:
        status = check_internet()

        if status and previous_status != "online":

            print("Status: online")  # Internet connect hone par ye message aayega
            speak( "We are online now!")
            previous_status = "online"

        elif not status and previous_status != "offline":
            print("Status: offline")  # Internet disconnect hone par ye message aayega
            speak( "We are offline sir!")
            previous_status = "offline"

        time.sleep(5)  # Har 5 second baad status check karega


