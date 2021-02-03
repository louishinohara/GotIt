import speech_recognition as sr

# Find your device's output and set that index in the sr.Microphone(device_index)
def findInputSource():      
    devices = sr.Microphone.list_microphone_names()

    for i in range(len(devices)):
        print(str(i) + ': ' + str(devices[i]))


