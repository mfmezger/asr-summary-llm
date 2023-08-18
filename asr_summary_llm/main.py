import whisper
from pyannote.audio import Pipeline

pipeline = Pipeline.from_pretrained('pyannote/speaker-diarization')

DEMO_FILE = {'uri': 'blabal', 'audio': 'audio.wav'}
dz = pipeline(DEMO_FILE)  

with open("diarization.txt", "w") as text_file:
    text_file.write(str(dz))
def main():
    pass

print(*list(dz.itertracks(yield_label = True))[:10], sep=&quot;\n&quot;)

if __name__ == "__main__":
    
    from pydub import AudioSegment

    t1 = 0 * 1000 # works in milliseconds
    t2 = 20 * 60 * 1000

    newAudio = AudioSegment.from_wav("download.wav")
    a = newAudio[t1:t2]
    a.export("audio.wav", format="wav") 


    main()