import os
import time
import playsound 
import speech_recognition as sr
from gtts import gTTS
import pyaudio 

def speak(text):        # Translates text to speach using google's library
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio_from_mic():   # Gets audio from mic and translates to text
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=None)
    with mic as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)

        except Exception as e:
            print("Exception: " + str(e))

    return said

def findInputSource():      # Find your device's output and set that index in the sr.Microphone(device_index)
    devices = sr.Microphone.list_microphone_names()

    for i in range(len(devices)):
        print(str(i) + ': ' + str(devices[i]))


def main():
    findInputSource()
    # speak('Play Recording Now')
    text = get_audio_from_mic()

# These next few lines of code can determine whether certain phrases exist in the text and triggers a function


    # if "payment" in text: 
    #     speak('Pulling Up Venmo')
    # else:
    #     speak(text)


main()



