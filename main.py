from ZoomClass import Zoom
from VoiceClass import Voice
from GCloudClass import GCloud


def main():
    voice = Voice()
    
    ZOOM_API_TOKEN = 'https://wmcc.zoom.us/closedcaption?id=99632027021&ns=VVNISU8gU0hJTk9IQVJBJ3MgWm9vbSBNZWV0aW5n&expire=86400&sparams=id%2Cns%2Cexpire&signature=YsUUv5r7YtmRRfzaNW_-B3P6TwQY6YFSbFct4C_ob1U.AG.HeFxpw9WeqLeDPMP_GczhAeiRT5iQJSs2V4DZVRDdI8w-eyiNmCLFtBYEKAnCPiveRsC6wycvwDVYTaVPOzBnzTySiaUudbOu4E_07_UsKk2OIa_Z3h1aFWM.294f0xnkWIFDqEqHLVzJow.MkZe635jQzX_jJrh'
    
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
    ZOOM_API_TOKEN = 'https://wmcc.zoom.us/closedcaption?id=93846635912&ns=VVNISU8gU0hJTk9IQVJBJ3MgWm9vbSBNZWV0aW5n&expire=86400&sparams=id%2Cns%2Cexpire&signature=PHmXZI3cvRMjRM9Oktx0nxTiisVcWKUnQGOL65a6FCo.AG.VUwdPapAw5cr9oHxJtkUobK0nHbbIx8oPvvZBZYq8F-9l0_xUSfBTF9Ad-GyPFFNOvyHbZCyNWKhWlSl8UPbbqnDUJOLvgRadGt-cXEi__luwfX3CS0HHHlw.0On0MGAO1tEbKLb2yYxQMQ.X0qHZwgQS6eobq38'
    
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
