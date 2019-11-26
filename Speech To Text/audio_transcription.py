import wave
import speech_recognition as sr
import contextlib
from difflib import SequenceMatcher

r = sr.Recognizer()

duration = 0
with contextlib.closing(wave.open('ted_talk_1.wav','r')) as f:
  frames = f.getnframes()
  rate = f.getframerate()
  duration = int(frames / float(rate))

test = sr.AudioFile('ted_talk_1.wav')
transcripts_file = open("transcripts.csv").read().split("\n")
del transcripts_file[0]
transcript = ""
original = transcripts_file[0][:transcripts_file[0].index('https') - 1]
introduction = 0

for i in range(0, int(duration / 5) + 1):
    with test as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source, offset=((i * 5) + introduction), duration=5)
    try:
        result = r.recognize_google(audio, show_all=True)
        if(result != []):
            text = result["alternative"][0]["transcript"] + " "
            transcript += result["alternative"][0]["transcript"] + " "
        else:
            transcript += " VALUE_ERROR "
    except sr.UnknownValueError:
        transcript += " VALUE_ERROR "

f = open("transcript.txt", "w+")
f.write(transcript)
f.close()

print("Similarity:")
print(SequenceMatcher(None, original, transcript).ratio())
