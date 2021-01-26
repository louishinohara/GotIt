import os
import time
import playsound 
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio_from_mic():
    r = sr.Recognizer()
    mic = sr.Microphone()
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
    # findInputSource()
    speak('Play Recording Now')
    text = get_audio_from_mic()


    # if "testing" in text:
    #     speak('Testing')
    # else:
    #     speak(text)


main()



