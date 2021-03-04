## Suraj's program to play snippets of files and test audio response time
import os
import time
import speech_recognition as sr
import pyaudio 
import requests
from playsound import playsound


def postTranscript(api_token, transcript):
    # https://github.com/heyyeh12/zoom_cc#development
    # Used this code as a sample to post to zoom

    post_params = {
        'seq' : 1,
        'lang' : "en-US"
    }
    
    r1 = requests.post(api_token,
        params=post_params, data=transcript,
        headers={'Content-type': 'text/plain; charset=utf-8'}
        )
    print('Text posted')

def getAudioFromMic(soundFile):   # Gets audio from mic and translates to text
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=2)     # Suraj's VoiceMeeter Output number

    with mic as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)

        except Exception as e:
            print("Exception: " + str(e))

    return said

def main():
    api_token = 'https://wmcc.zoom.us/closedcaption?id=4284297067&ns=U3VyYWogU2FueWFsJ3MgUGVyc29uYWwgTWVldGlu&expire=86400&sparams=id%2Cns%2Cexpire&signature=3nnYJlDGDD3_fAEmDxr5DYU5bfWqbKgsb7gSGS4nd_U.AG.UCDXx1lGm4Tjzyk7iN9vFYswi6CIofl3pjCS90oSG6LMhWy9htqtGaiCQxUrw4abnm3hv6Kd3cHDTvnEBEVA816szTtQFhuokdcpa5UHKQKIqyuIX1S_Og.i-vVjuBc3KYcP0D1p9pCRQ.SMSXOpxAbiQ3JZY1'



    for i in range(5):
        snippet = "audioSnippets/excerpts/ex" + str(i+1) + ".mp3"
        playsound(snippet)
        # text = getAudioFromMic(snippet)
        # getAnalysis(text)
        # postTranscript(api_token, text)
    

main()