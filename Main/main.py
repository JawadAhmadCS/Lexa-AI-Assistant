from colorama import Fore
import threading
from my.brain.recognize import recognize
from my.brain.welcome import welcome
from my.head.listen import listen
from my.Automation.online_offline import monitor_connection
from my.Animation.LexaWellcome import start_welcome_animation
start_welcome_animation()
# Welcome message
welcome()


def main():
    try:
        while True:
            # Get user input
            user_input = listen()
            print(Fore.RED + user_input)

            # Handle unrecognized input
            if user_input == "\rSorry, I didn't understand that.":
                main()
            if user_input == "\rCould not request results from Speech Recognition service.":
                user_input = input("Please provide text input: ")
            recognize(user_input)



    except Exception as e:
        print(f"An error occurred: {str(e)}")


t1 =threading.Thread(target=main)
t2=threading.Thread(target=monitor_connection)
t1.start()
t2.start()
t1.join()
t2.join()