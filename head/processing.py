import requests
import webbrowser
import threading
from wikipedia import wikipedia
from my.Data.model import mind
from my.head.Speak import speak
from my.Modules.google_search import google_search
from my.Modules.wikipedia_search import wiki_search
#from my.process.wellcome import welcome
from colorama import Fore, Style, init
#welcome()
def load_qa_data(file_path):
    qa_dict = {}
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(":")
            if len(parts) != 2:
                continue
            q, a = parts
            qa_dict[q] = a
    return qa_dict

qa_file_path = r"C:\Users\mjawa\Pictures\Lexa\my\Data\tqna.txt"
qa_dict = load_qa_data(qa_file_path)
#print(qa_dict)
# print animated message
def save_qa_data(file_path, qa_dict):
    with open(file_path, "w", encoding="utf-8") as f:
        for q, a in qa_dict.items():
            f.write(f"{q}:{a}\n")
def print_animated_message(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.075)  # Adjust the sleep duration for the animation speed
    print()

def process(text):
    try:
        response = mind(text)
        #print(response)
        # Start animation and speaking concurrently
        #animate_thread = threading.Thread(target=print_animated_message, args=(response,))
        #speak_thread = threading.Thread(target=speak, args=(response,))
        #speak_thread.start()
        #speak_thread.join()

        qa_dict[text] = response  # Store in qa_dict
        save_qa_data(qa_file_path, qa_dict)  # Save updated qa_dict
        return response
    except Exception as e:
        #print(f"An error occurred: {str(e)}")
         return Fore.RED+f"An error occurred: {str(e)}"
#while True:
#x=input()
# x="SRK"
#process(x)
#wiki_search("Jawad Ahmad")
#google_search("who is jawad ahmad")