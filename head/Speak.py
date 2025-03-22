import asyncio #as ka andr await lgana sa code ko pause
import threading
import os
import time

import edge_tts  # pip install edge-tts
import pygame

VOICE = "en-AU-WilliamNeural"
BUFFER_SIZE = 1024

def remove_file(file_path):
    max_attempt = 3
    attempts = 0
    while attempts < max_attempt:
        try:
            with open(file_path, "wb"):
                pass#mean ka andr koi operationnhi ha
            os.remove(file_path)
            break
        except Exception as e:
            #print(f"Error: {e}")
            return f"Error: {e}"
            attempts += 1

async def amain(TEXT, output_file) -> None:
    try:
        cm_txt = edge_tts.Communicate(TEXT, VOICE)
        await cm_txt.save(output_file)
        thread = threading.Thread(target=play_audio, args=(output_file,))
        thread.start()
        thread.join()
    except Exception as e:
        #print(f"Error: {e}")
         return f"Error: {e}"
    finally:
        remove_file(output_file)

def play_audio(file_path):
    try:
       # pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound(file_path)
        sound.play()
        while pygame.mixer.get_busy():  # Keep looping while the audio is playing
            pygame.time.wait(100)  # Wait 100 milliseconds
        pygame.quit()  # Quit only after playback finishes
    except:# Exception as e:
        return
      #  print(f"Error: {e}")


def speak(TEXT, output_file=None):
    if output_file is None:
        output_file = f"{os.getcwd()}/speak.mp3"#OS sa currnt working dirctory mang rha .../home/user/project/speak.mp3
    asyncio.run(amain(TEXT, output_file))
    #this function  just that i dont need speaking so i dont proceed for speaking use above function
def speak1(TEXT, output_file=None):
    a=2

# Example usage
#speak("Wellcome sir jawad")

