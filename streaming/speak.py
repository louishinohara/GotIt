from gtts import gTTS
import playsound 

def speak(text):        # Translates text to speach using google's library
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

