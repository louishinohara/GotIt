import time
import requests

# https://github.com/heyyeh12/zoom_cc#development

class Zoom:
    def __init__(self, apiToken):
        self.seq_num = 340                                           # Acts like a key when sending HTTPS Posts
        self.api_token = apiToken
        self.session = requests.Session()                               # Keeps open session
        self.params = {'seq' : str(0), 'lang' : "en-US" }               # For POST
        self.headers = {'Content-type': 'text/plain; charset=utf-8'}    # For POST
        for _ in range(2):
            self.post_transcript("Initializing Got It! ")

    # def __exit__(self, exception_type, exception_value, traceback):
    #     self.save_config()
    #     print("{}Exiting. Last sequence sent = {} {}".format(self.YELLOW, self.seq_count, self.RESET))

    def increase_seq_num(self):                                         # Increase the seq number and params for POST
        self.seq_num += 1
        self.params = {'seq' : str(self.seq_num), 'lang' : "en-US" }
    
    def post_transcript(self, transcript):
        self.session.post(self.api_token, params=self.params, data=transcript, headers=self.headers)    # Post transcript
        self.increase_seq_num()     # Increment Seq Num
        print("[seq #] " + str(self.seq_num))
        time.sleep(1.5)             # Sleep so the API is not overloaded with requests