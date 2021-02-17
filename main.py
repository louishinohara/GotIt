from findInputSource import findInputSource
from speak import speak
from getAudio import getAudioFromMic
from getAnalysis import getAnalysis
from postToZoom import postTranscript
import requests
import time

def main():
    findInputSource()
    # speak('Play Recording Now')
    keepGoing = True
    api_token = 'https://wmcc.zoom.us/closedcaption?id=99766787474&ns=VVNISU8gU0hJTk9IQVJBJ3MgWm9vbSBNZWV0aW5n&expire=86400&sparams=id%2Cns%2Cexpire&signature=7PkopQpxFgXxIfGtUx9_1PfHVFWywC_Ni0t1eYgFhjA.AG.HG97mnkVM26s8kceuEeukAf8gD1WMPZQ1_4GJPdlp41JrSo1VF1D3oeiwBpREdhUtPiWHkddldO00IiqaLFDwuugFs87YUTR-AGQrL_k0WeI77c4OdOskkwC.5VVWewsvw6jVetJG4WPiyQ.DPus7C6RE0mLTNNK'


    session = requests.Session()
    seqNum = 1
    for i in range(10):
        text = getAudioFromMic()
        print(text)
        # getAnalysis(text)
        # text = 'Text Number'
        # textToSend = text+ ': ' + str(seqNum)
        postTranscript(api_token, text, session, seqNum)
        seqNum += 1
        time.sleep(1.2)
    

main()
