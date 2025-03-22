import webbrowser
from my.head.Speak import speak
from my.Data.dlg import websites
def browse(input):
    try:
        webbrowser.open(websites[input])
        #print("Done! " + input +"  is now open for you" )
        return ("Done! " + input +"  is now open for you")

    except Exception as e:
        return f"\rAn error occurred: {e}"


#input="google"
#browse(input)