import speech_recognition as sr
from mtranslate import translate
#import threading
import time
from colorama import Fore, Style, init
init(autoreset=True)
recognizer = sr.Recognizer()

# Voice accuracy improvement settings
recognizer.dynamic_energy_threshold = True   # Let it adjust sensitivity automatically
recognizer.energy_threshold = 300            # Default energy threshold (adjust if needed)
recognizer.dynamic_energy_adjustment_damping = 0.15  # Moderate adjustment speed
recognizer.dynamic_energy_ratio = 1.5        # Slightly more sensitive to speech than noise
recognizer.pause_threshold = 0.8             # Allows natural pauses during speech
recognizer.operation_timeout = None           # No timeout (listens indefinitely)
recognizer.non_speaking_duration = 0.5       # Standard duration of silence before stopping

def Trans_hindi_to_english(txt):
    return translate(txt, to_language="in-en")

# Function to listen for audio input and process it
def listen():
    with sr.Microphone() as source:  # Using the microphone as the audio source
        recognizer.adjust_for_ambient_noise(source)
        print(Fore.LIGHTGREEN_EX+"I am Listening...", end="", flush=True)
        try:
            audio = recognizer.listen(source, timeout=None)
            print("\rGot it, Now Recognizing...", end="", flush=True)
            recognized_txt = recognizer.recognize_google(audio).lower()
            if recognized_txt:
                translated_txt = Trans_hindi_to_english(recognized_txt)
                #print( Fore.GREEN +"\rSir Jawad You said: " + translated_txt)
                return translated_txt
            else:
                print("")
        except sr.UnknownValueError:
             #print(Fore.RED+"\rSorry, I didn't understand that.")
             return "\rSorry, I didn't understand that."
        except sr.RequestError:
            #print(Fore.RED+"\rCould not request results from Speech Recognition service.")
            return "\rCould not request results from Speech Recognition service."

# Function to continuously listen for audio input
#def listen_loop():
#    while True:
#        listen()
        #time.sleep(1)  # Optional: slight delay before listening again
#listen()
# Create and start the listening thread
#listen_thread = threading.Thread(target=listen_loop)
#listen_thread.start()
#listen_loop()
# Main program can do other tasks here (if any)
#try:
#    while True:
#        time.sleep(1)  # Keep the main thread alive
#except KeyboardInterrupt:
#    print("\nProgram terminated.")
