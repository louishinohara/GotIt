import os
import time
import pyaudio 
import playsound 
from gtts import gTTS
import speech_recognition as sr


class Voice:
    def __init__(self):
        self.temp = 0

    def findInputSource(self):  # Find input sources for Voicemeeter Virtual Mic    
        devices = sr.Microphone.list_microphone_names()
        for i in range(len(devices)):
            print(str(i) + ': ' + str(devices[i]))

    def speak(self, text):        # Translates text to speach using google's library
        tts = gTTS(text= text, lang= "en")  # Converts text to speech
        filename = "voice.mp3"              # Creates a new mp3 file
        tts.save(filename)                  # Saves text to mp3 file as sound
        playsound.playsound(filename)       # Plays sound

    def getAudioFromMic(self):   # Gets audio from mic and translates to text
        r = sr.Recognizer()
        mic = sr.Microphone(device_index= 2)    # Default is set to None

        with mic as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)

            except Exception as e:
                print("Exception: " + str(e))

        return said

    def analyzeText(self, text):
        # These next few lines of code can determine whether certain phrases exist in the text and triggers a function
        if "hello" in text: 
            print('Hello There')
        elif "goodbye" in text:
            print("Good Bye")

        return