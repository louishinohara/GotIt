
from ZoomClass import Zoom
from VoiceClass import Voice

def main():
    voice = Voice()


    api_token = 'https://wmcc.zoom.us/closedcaption?id=94627603448&ns=VVNISU8gU0hJTk9IQVJBJ3MgWm9vbSBNZWV0aW5n&expire=86400&sparams=id%2Cns%2Cexpire&signature=c1v4xoLvBdDXgT7pasbJ0KBx05SaajvYMTd-ctsZyb8.AG.SFklqR-FQajIVfAd30QcJPLS8DlDEyjrHiZTkoBoFjbZAWbqAIoAknE4oTscOssnNlxYutnsE43qh8n-0ZY8ZUG_CQ82nqn4IT0TGDtjN6QrRNHHoSuqrIs8.t8sHI_c-P3vhspDVeCNzRQ.AwLua5mWe3uMJGuJ'
    
    zoom = Zoom(api_token)

    for i in range(10):
        text = voice.getAudioFromMic()
        zoom.post_transcript(text)

main()


# Other possible methods from Voice class
    # voice.findInputSource()
    # voice.speak('Play Recording Now')
    # voice.analyzeText(text)
