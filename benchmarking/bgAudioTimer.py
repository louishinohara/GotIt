## from https://reposhub.com/python/miscellaneous/realpython-codetiming.html
import logging
from codetiming import Timer
import speech_recognition as sr


# ## from https://github.com/Uberi/speech_recognition/blob/master/examples/background_listening.py
# ## off of https://pypi.org/project/SpeechRecognition/

# import time
# import speech_recognition as sr


# # this is called from the background thread
# def callback(recognizer, audio):
#     # received audio data, now we'll recognize it using Google Speech Recognition
#     try:
#         # for testing purposes, we're just using the default API key
#         # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#         # instead of `r.recognize_google(audio)`
#         print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio))
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))


# r = sr.Recognizer()
# m = sr.Microphone(device_index=2)
# with m as source:
#     r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
# print('0. calibration done')
# # start listening in the background (note that we don't have to do this inside a `with` statement)
# stop_listening = r.listen_in_background(m, callback)
# # `stop_listening` is now a function that, when called, stops background listening
# print('1. listening in bg')
# # do some unrelated computations for 5 seconds
# for _ in range(50): time.sleep(0.1)  # we're still listening even though the main thread is doing other things
# print('2. sleep done')
# # calling this function requests that the background listener stop listening
# stop_listening(wait_for_stop=False)
# print('3. listen stopped.')
# # do some more unrelated things
# for _ in range (100): time.sleep(0.1)  # we're not listening anymore, even though the background thread might still be running for a second or two while cleaning up and stopping

## from https://pypi.org/project/SpeechRecognition/1.2.3/
def callback(recognizer, audio):                          # this is called from the background thread
    print('recognizer called')
    with t:
        try:
            print("You said " + recognizer.recognize_google(audio))  # received audio data, now need to recognize it
        except LookupError:
            print("Oops! Didn't catch that")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

t = Timer("example", text="Time spent: {:.2f}", logger=logging.warning)

r = sr.Recognizer()
m = sr.Microphone(device_index=2)
with m as source:
    with t:
        r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
        print('calibrated')
    
print('listening')
r.listen_in_background(m, callback)     ## TODO: Automate this r.listen_in_background with stop_listening = r.listen_in_background(m, callback)

import time
while True: time.sleep(0.1)                         # we're still listening even though the main thread is blocked