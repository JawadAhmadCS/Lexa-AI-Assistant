import random
from my.Data.dlg import welcomedlg
from my.head.Speak import speak
def welcome():
    welcome = random.choice(welcomedlg)
    print(welcome)
    speak(welcome)