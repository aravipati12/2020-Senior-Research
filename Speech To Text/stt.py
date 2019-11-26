import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pydub import AudioSegment

introduction = 12
time_introduction = introduction * 1000 #Works in milliseconds
to_translate = AudioSegment.from_mp3('ted_talk_7.mp3')
to_translate = to_translate[time_introduction:]
to_translate.export('ted_talk_7_to_translate.mp3', format='mp3')

authenticator = IAMAuthenticator('VVphAIuuzYGYOtHwblE53e_UARSq1F_nqQBe_HwpyRL7')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)
speech_to_text.set_service_url('https://gateway-wdc.watsonplatform.net/speech-to-text/api')

class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_data(self, data):
        transcript = ""
        for i in range(len(data["results"])):
            transcript += data["results"][i]["alternatives"][0]["transcript"]
        f = open("transcript.txt", "w+")
        f.write(transcript)
        f.close()

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))

myRecognizeCallback = MyRecognizeCallback()

with open(join(dirname(__file__), 'ted_talk_7_to_translate.mp3'), 'rb') as audio_file:
    audio_source = AudioSource(audio_file)
    speech_to_text.recognize_using_websocket(
        audio=audio_source,
        content_type='audio/mp3',
        recognize_callback=myRecognizeCallback,
        model='en-US_BroadbandModel')
