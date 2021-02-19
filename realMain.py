from findInputSource import findInputSource
from speak import speak
from getAudio import getAudioFromMic
from getAnalysis import getAnalysis
from postToZoom import postTranscript

def main():
    # findInputSource()
    # speak('Play Recording Now')
    api_token = 'https://wmcc.zoom.us/closedcaption?id=4284297067&ns=U3VyYWogU2FueWFsJ3MgUGVyc29uYWwgTWVldGlu&expire=86400&sparams=id%2Cns%2Cexpire&signature=3nnYJlDGDD3_fAEmDxr5DYU5bfWqbKgsb7gSGS4nd_U.AG.UCDXx1lGm4Tjzyk7iN9vFYswi6CIofl3pjCS90oSG6LMhWy9htqtGaiCQxUrw4abnm3hv6Kd3cHDTvnEBEVA816szTtQFhuokdcpa5UHKQKIqyuIX1S_Og.i-vVjuBc3KYcP0D1p9pCRQ.SMSXOpxAbiQ3JZY1'



    for i in range(5):

        text = getAudioFromMic()
        # getAnalysis(text)
        postTranscript(api_token, text)
    

main()
