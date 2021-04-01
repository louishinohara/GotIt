from ZoomClass import Zoom
from VoiceClass import Voice
from GCloudClass import GCloud


def main():
    voice = Voice()
    voice.speak('beep')
    ZOOM_API_TOKEN = 'https://wmcc.zoom.us/closedcaption?id=2172132419&ns=Sm9zaHVhIEh5bW93aXR6J3MgUGVyc29uYWwgTWVl&expire=86400&sparams=id%2Cns%2Cexpire&signature=N7VY_l70shwwdsunIQAVuzg1yB8pdWT5XN6c9hxoY6U.AG.NwznwpdVzs3cKNJNI3v1696l7qZlhw0nSqGYSpZENFA6PODVspBiWvbHhh-NwsC1EnuYjX_6QyPukAcnZJsb_GdB_FHQqlwW31X6L3VA7VxWFwBwvMZYAQ.n0pYxcys94Lf6hvYexkAgQ.GrTmW8tnf4DFODVv'
    
    zoom = Zoom(ZOOM_API_TOKEN)

    for i in range(10):
        # text = voice.getAudioFromMic()
        text = "Text Text # " + str(i)
        zoom.post_transcript(text)

def testGCloud():

    # Audio recording parameters
    RATE = 16000
    CHUNK = int(RATE / 10)  # 100ms
    language_code = "en-US"
    ZOOM_API_TOKEN = 'https://wmcc.zoom.us/closedcaption?id=2172132419&ns=Sm9zaHVhIEh5bW93aXR6J3MgUGVyc29uYWwgTWVl&expire=86400&sparams=id%2Cns%2Cexpire&signature=N7VY_l70shwwdsunIQAVuzg1yB8pdWT5XN6c9hxoY6U.AG.NwznwpdVzs3cKNJNI3v1696l7qZlhw0nSqGYSpZENFA6PODVspBiWvbHhh-NwsC1EnuYjX_6QyPukAcnZJsb_GdB_FHQqlwW31X6L3VA7VxWFwBwvMZYAQ.n0pYxcys94Lf6hvYexkAgQ.GrTmW8tnf4DFODVv'
    
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
