from ZoomClass import Zoom
from VoiceClass import Voice
from GCloudClass import GCloud
from sqlquery import databaseQuery


def main():
    # voice = Voice()
    # voice.speak('beep')
    ZOOM_API_TOKEN = 'https://wmcc.zoom.us/closedcaption?id=2172132419&ns=Sm9zaHVhIEh5bW93aXR6J3MgUGVyc29uYWwgTWVl&expire=86400&sparams=id%2Cns%2Cexpire&signature=Q2juRWo0cFpVbX9NfEVbet0wOfZtgEvl5-JxlpoZOEA.AG.Nej1zhAaLZGHL0lcf6x-FTfZQyci4GuDexY9R-eMAhy15RK3CHuGQ9Y1d-9ZAVR82Y2-yhZdhjkI7OrYxjxml2TbRZEzZ6LthCnGEHdcfpR6T-5W2u6rNw.ddXkFWA69V1hIac2t8qTyg.5Md7B7fkmlD6bWTh'
    
    seq_token = databaseQuery.getAPITokens(databaseQuery, ZOOM_API_TOKEN)

    zoom = Zoom(ZOOM_API_TOKEN, seq_token)

    for i in range(5):
        # text = voice.getAudioFromMic()
        text = "STRING " + str(i) + " "
        zoom.post_transcript(text)

def testGCloud():

    # Audio recording parameters
    RATE = 16000
    CHUNK = int(RATE / 10)  # 100ms
    language_code = "en-US"
    ZOOM_API_TOKEN = 'https://wmcc.zoom.us/closedcaption?id=2172132419&ns=Sm9zaHVhIEh5bW93aXR6J3MgUGVyc29uYWwgTWVl&expire=86400&sparams=id%2Cns%2Cexpire&signature=Q2juRWo0cFpVbX9NfEVbet0wOfZtgEvl5-JxlpoZOEA.AG.Nej1zhAaLZGHL0lcf6x-FTfZQyci4GuDexY9R-eMAhy15RK3CHuGQ9Y1d-9ZAVR82Y2-yhZdhjkI7OrYxjxml2TbRZEzZ6LthCnGEHdcfpR6T-5W2u6rNw.ddXkFWA69V1hIac2t8qTyg.5Md7B7fkmlD6bWTh'
    seq_token = databaseQuery.getAPITokens(databaseQuery, ZOOM_API_TOKEN)

    zoom = Zoom(ZOOM_API_TOKEN, seq_token)
    g = GCloud(RATE, CHUNK, language_code)
    # g.testLocalAudio()

    g.getStreamedTranscription(zoom)

testGCloud()
# main()


# Other possible methods from Voice class
    # voice.findInputSource()
    # voice.speak('Play Recording Now')
    # voice.analyzeText(text)
