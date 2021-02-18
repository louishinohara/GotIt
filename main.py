from ZoomClass import Zoom
from VoiceClass import Voice

def main():
    voice = Voice()
    
    ZOOM_API_TOKEN = 'https://wmcc.zoom.us/closedcaption?id=98437352608&ns=VVNISU8gU0hJTk9IQVJBJ3MgWm9vbSBNZWV0aW5n&expire=86400&sparams=id%2Cns%2Cexpire&signature=NgLdApYNHJjm4RSR94vBzCY9zJUs8LfZ6YF7ObPkMG0.AG.4iLRBdx-KPT0RCbRqJ4jjImSClQm9iVYKJ5ri3qfTQ2ksQYBsAFJS8pZJsYnPcWFAeqZNDJjo4pKmArRgvIUSvc7t5TvKzpiqZonEbVql53IWzhmJrcAzPf-.Ih13_b5eHAxa4dawmfy5IA.ueB1PKYSYix46tqa'
    
    zoom = Zoom(ZOOM_API_TOKEN)

    for i in range(10):
        # text = voice.getAudioFromMic()
        text = "Test Text # " + str(i) + "ly dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially uncha"
        zoom.post_transcript(text)

main()


# Other possible methods from Voice class
    # voice.findInputSource()
    # voice.speak('Play Recording Now')
    # voice.analyzeText(text)
