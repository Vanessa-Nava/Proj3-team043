import wave
import numpy as np 
import soundfile as sf
from scipy.fftpack import fft
import pymatlab.matlab 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def frequencies():
    wave_file= wave.open("iCry (1).wav") #open wave file
    rate, sound= sf.read("iCry (1).wav") #read in rate and sound using sounfile
    sf.write('new_file.wav',rate, sound) #write in a new wav file

   print(sound) #gives the sample rate in Hz
    print (rate) #gives all the frequencies

   framerate= wave_file.getframerate()
    frames= wave_file.getnframes()
    width= wave_file.getsampwidth()

   print("sampling rate: ", framerate, "Hz")
    print("length: ", frames, "samples")
    print("sample width: ", width, "bytes")


   #getting the data to calculate the time of sound
    t= np.arange(len(rate))/float(sound)

   #plotting the info
    plt.figure(figsize=((20),4 ))
    plt.fill_between(t, rate[:,0], rate[:,1], color='b')
    plt.xlim(t[0], t[-1])
    plt.xlabel("time (sec)")
    plt.ylabel("amplitude")
    plt.savefig('plot.png', dpi=100)
    plt.show()
