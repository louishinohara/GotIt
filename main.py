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
    api_token = 'https://us02wmcc.zoom.us/closedcaption?id=89484164831&ns=UlUgQ2Fwc3RvbmUgTWVldGluZw&expire=86400&sparams=id%2Cns%2Cexpire&signature=h12-VMcwuacjziG3-SkXG63EPGwM4srSyTK9hCGJJZY.AG.tld7wbYR42uz1MSy7wLhMOYmL5F1tXBvHNT6mS1iTKkuxHIBK0HoZEvRkIBjIvDBqPlAoaedCmKKm5LXBy68DClS3CwPIBU.5nXjAhnUbVs4hyR4cBOzfQ.q5-Z1fUcYCppAnrQ'
    t = Timer("example", text="Time spent: {:.2f}", logger=logging.warning)

    for _ in range(5):

        text = "example"
        # getAnalysis(text)
        
        with t:
            postTranscript(api_token, text)
            

main()
