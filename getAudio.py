import os
import time
import speech_recognition as sr
import pyaudio 

def getAudioFromMic():   # Gets audio from mic and translates to text
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=2)
    # mic = sr.Microphone(device_index=None)


    with mic as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)

        except Exception as e:
            print("Exception: " + str(e))

    return said



