import os.path as path
from traceback import print_exc
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.websocket import RecognizeCallback, AudioSource
import json

response = None

class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_data(self, data):
        global response
        response = json.dumps(data, indent=3).encode('utf-8')

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))

myRecognizeCallback = MyRecognizeCallback()

def convert(lesson_file, json_file=None):
    global response
    try:
        if not isinstance(lesson_file, str):
            raise TypeError('lesson_file argument type must be a string and end with .wav (audio file)')
        if not path.exists(lesson_file):
            raise FileNotFoundError('the lesson file path does not exist')
        # 20/12/2020 16:30
        # print(basename + ', ' + json_file)
        if json_file == None:
            basename = path.basename(lesson_file)
            json_file = basename.replace(basename.split('.')[-1], 'json')

        # 20/12/2020 20:20
        #speech recognition
        sr = ibm_speechrecognition()
        with open(lesson_file, 'rb') as audio_file:
            audio_source = AudioSource(audio_file)
            sr.recognize_using_websocket(
                audio=audio_source,
                content_type='audio/wav',
                recognize_callback=myRecognizeCallback,
                model='it-IT_BroadbandModel',
                max_alternatives=3,
                inactivity_timeout=-1
            )
        
        # 20/12/2020 20:35
        # save to json file
        with open(f'json/{json_file}', 'wb') as f:
            f.write(response)

    except Exception as e:
        print_exc()

def ibm_speechrecognition():
    authenticator = IAMAuthenticator(apikey='Wjfeh8MOpjxMLni5J7z2PUEhKdcMx37_RbNFyeRIIdFI')
    speech_to_text = SpeechToTextV1(
        authenticator=authenticator
    )

    speech_to_text.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/396893f9-f64c-46a6-8893-51ca2d7927a2')
    return speech_to_text