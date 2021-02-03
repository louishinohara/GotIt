from findInputSource import findInputSource
from speak import speak
from getAudio import getAudioFromMic
from getAnalysis import getAnalysis
from postToZoom import postTranscript

def main():
    # findInputSource()
    # speak('Play Recording Now')
    keepGoing = True
    api_token = 'https://wmcc.zoom.us/closedcaption?id=99211570681&ns=VVNISU8gU0hJTk9IQVJBJ3MgWm9vbSBNZWV0aW5n&expire=86400&sparams=id%2Cns%2Cexpire&signature=xhouuJ1_oVm6g6zo1qZ0-1umW37xxtR-OQ8wJ83uINA.AG.Qurhu1AvwaiKL0Zb4SsIH6Y6d68Eotn6eIPJUJzeq6xmpF4G2NQX8Cl35bibNM7ESoyd2wtz86bc1y5BkpvUp7YheOFGchJTzYP3m7NAqUNQkDCmMhU30OWn.JPDT-e80tIuPkixHP55cuw.wV4vT0rfh9GRYsV8'

    for i in range(5):
        text = getAudioFromMic()
        getAnalysis(text)
        postTranscript(api_token, text)
    

main()
