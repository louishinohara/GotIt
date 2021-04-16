from ZoomClass import Zoom
from VoiceClass import Voice
from GCloudClass import GCloud


def main():
    # voice = Voice()
    # voice.speak('beep')
    ZOOM_API_TOKEN = 'https://wmcc.zoom.us/closedcaption?id=2172132419&ns=Sm9zaHVhIEh5bW93aXR6J3MgUGVyc29uYWwgTWVl&expire=86400&sparams=id%2Cns%2Cexpire&signature=JCw7i8gtSxqGeklgU19ETm6wliDGdgudwkvhWI0Eq_k.AG.rnsAw6fY3xKd0lRsNZtIFsGRd_myZnHnFeM_3X9Kc9R35WbW_EsnZin16PcZ0ni0ki--fxkdymRQylxCR9wkKjtQykxWasgY2_dZAO3vGw7zpBZIAuFGnA.YEoanSsVo_2KaWnhK5JmQw.Zgz0mW8lZ6ZvyXMG'
    
    zoom = Zoom(ZOOM_API_TOKEN)

    for i in range(5):
        # text = voice.getAudioFromMic()
        text = "STRING " + str(i) + " "
        zoom.post_transcript(text)

def testGCloud():

    # Audio recording parameters
    RATE = 16000
    CHUNK = int(RATE / 10)  # 100ms
    language_code = "en-US"
    ZOOM_API_TOKEN = 'https://wmcc.zoom.us/closedcaption?id=2172132419&ns=Sm9zaHVhIEh5bW93aXR6J3MgUGVyc29uYWwgTWVl&expire=86400&sparams=id%2Cns%2Cexpire&signature=JCw7i8gtSxqGeklgU19ETm6wliDGdgudwkvhWI0Eq_k.AG.rnsAw6fY3xKd0lRsNZtIFsGRd_myZnHnFeM_3X9Kc9R35WbW_EsnZin16PcZ0ni0ki--fxkdymRQylxCR9wkKjtQykxWasgY2_dZAO3vGw7zpBZIAuFGnA.YEoanSsVo_2KaWnhK5JmQw.Zgz0mW8lZ6ZvyXMG'
    
    zoom = Zoom(ZOOM_API_TOKEN)
    g = GCloud(RATE, CHUNK, language_code)
    # g.testLocalAudio()

    g.getStreamedTranscription(zoom)

testGCloud()
# main()


# Other possible methods from Voice class
    # voice.findInputSource()
    # voice.speak('Play Recording Now')
    # voice.analyzeText(text)
