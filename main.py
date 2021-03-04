## SURAJ'S TEST FOR ZOOM OUTPUT
import logging
from codetiming import Timer
from datetime import datetime

from findInputSource import findInputSource
from speak import speak
from getAudio import getAudioFromMic
from getAnalysis import getAnalysis
from postToZoom import postTranscript

def main():
    # findInputSource()
    # speak('Play Recording Now')
    api_token = 'https://wmcc.zoom.us/closedcaption?id=4284297067&ns=U3VyYWogU2FueWFsJ3MgUGVyc29uYWwgTWVldGlu&expire=86400&sparams=id%2Cns%2Cexpire&signature=zDazCC4yu2PQuN9HAvPRyeTtiMNOXUl0k6yxlT7jTNI.AG.6Ff85imlHcJ8Ky3rpB4LI7tLs9xkWl2CxN_UiL3dZg8n2VrPPXUA1meIRHSy0pp-zAM6O2VVuo4yhZx4rLLApocQjBC0h6dxvxgEx4OArcjd4mdSdGuEaw.TuDDDSot5Hb1BslVrNfW2g.TwKgnfmfg7cpbetu'
    # t = Timer("example", text="Time spent: {:.2f}", logger=logging.warning)

    for _ in range(5):

        text = getAudioFromMic()
        # getAnalysis(text)
        postTranscript(api_token, text)
            

main()
