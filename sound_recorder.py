import pyaudio
import audioop 
import wave
import collections
import numpy as np
import soundfile as sf
#import sys
import SpeechRecognition as sr

#CHUNK=  512 # by using the ASCII table for the wave sound file as bytes
#wave_file= wave.open("iCry.wav")
r = sr.Recognizer()
with sr.Microphone(device_index = 2, sample_rate = 44100, chunk_size = 512) as source:
    print("Say something!")
    audio = r.listen(source)


'''swidth= wave_file.getsampwidth()
RATE= wave_file.getframerate() 
CHANNELS= wave_file.getnchannels()
Record_Sec= 17


#using a blackman window to go through array
window= np.blackman(CHUNK)
sys.exit("EXIT......")
audio= pyaudio.PyAudio()

stream= audio.open(format= audio.get_format_from_width(wave_file.getsampwidth()),
                   CHANNELS= wave_file.getnchannels(), RATE=wave_file.getframerate(), output= True)

sf= collections.deque(maxlen= RATE/CHUNK)
#find the frequency of each chunk 
flag= True 
print( "Listening... ")
for i in range(0, int(RATE/CHUNK* Record_Sec)):
    data=stream.read(CHUNK)
    sf.append(abs(audioop.avg(data,4)))
    
print(sum(sf)/RATE/CHUNK*Record_Sec)

stream.stop_stream()
stream.close()
audio.terminate()

def listen():
    audio=pyaudio.PyAudio()
    audio.open(format= audio.get_format_from_width(wave_file.getsampwidth()),
                   CHANNELS= wave_file.getnchannels(), RATE=wave_file.getframerate(), input= True)

    sf=collections.deque(maxlen= RATE/CHUNK)
    flag=True;
    print("Listening... ")
    
    while(True):
        data= stream.read(CHUNK)
        sf.append(abs(audioop.avg(data,4)))
        if(flag==True):
            if (sum(sf)/(RATE/CHUNK*Record_Sec) < 5500000):
                print("off")
                flag=False 
                
        else:
            if(sum(sf)/(RATE/CHUNK*Record_Sec) > 5500000):
                print("on")
                flag=True'''
                
   
