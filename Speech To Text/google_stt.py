from google.cloud import speech_v1p1beta1
from google.cloud.speech_v1 import enums
from google.cloud import storage
from pydub import AudioSegment
import io, os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="Test1-f025040650eb.json"

mp3_audio = AudioSegment.from_file("audio/speech.mp3", format="mp3")  # sys.argv[1]
mp3_audio.export("audio/audio.flac", format="flac")

storage_client = storage.Client()
bucket = storage_client.bucket("ted_talks")
blob = bucket.blob("audio")
blob.upload_from_filename("audio/audio.flac")


client = speech_v1p1beta1.SpeechClient()
encoding = enums.RecognitionConfig.AudioEncoding.FLAC
language_code = "EN_US"
enable_automatic_punctuation = True

config = {
    "encoding": encoding,
    "language_code": language_code,
    "enable_automatic_punctuation": enable_automatic_punctuation
}

audio = {
    "uri": "gs://ted_talks/audio"
}

operation = client.long_running_recognize(config, audio)
response = operation.result()
transcript = ""
for result in response.results:
    alternative = result.alternatives[0]
    transcript += alternative.transcript.strip() + " "

f = open("new_transcript.txt", "w+")
f.write(transcript)
f.close()
