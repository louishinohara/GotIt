import requests

# https://github.com/heyyeh12/zoom_cc#development
# Used this code as a sample to post to zoom

def postTranscript(api_token, transcript, session, seqNum):
    
    post_params = {
        'seq' : str(seqNum),
        'lang' : "en-US"
    }
    r1 = session.post(api_token,
        params=post_params, data=transcript,
        headers={'Content-type': 'text/plain; charset=utf-8'}
        )
    print('Text posted')
