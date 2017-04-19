import pyaudio
import wave

def sound_audio():
FORMAT=pyaudio.get_sample_size
RATE=44100
CHUNK=1024
RECORD_SECONDS=17
WAVE_OUTPUT_FILENAME="iCry"

audio= pyaudio.PyAudio()

#start recording 
stream= audio.open(format=FORMAT,rate=RATE,input=True, frames_per_buffer=CHUNK)
print "recording.."
frames= []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print "finished recording"
 
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'iCry')
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()