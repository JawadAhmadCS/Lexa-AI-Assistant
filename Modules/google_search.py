import webbrowser
from my.head.Speak import speak
def google_search(query):
    if query:
        # Create Google search URL
        url = "https://www.google.com/search?q=" + query
        webbrowser.open_new_tab(url)
        print("You can see search results for " + query + " in Google on your screen.")
        speak("You can see search results for " + query + " in Google on your screen.")
        # Commenting out the speak function as it's not provided here
    else:
        speak("I didn't catch what you said.")
        # Commenting out the speak function as it's not provided here
        print("I didn't catch what you said.")
#google_search("Ronaldo")