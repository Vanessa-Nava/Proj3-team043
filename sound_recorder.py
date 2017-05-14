import wave
import numpy as np 
import soundfile as sf
from scipy.fftpack import fft
import pymatlab.matlab 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#1,000 to 5,000 Hz average is 3,500Hz

wave_file= wave.open("iCry (1).wav")
rate, sound= sf.read("iCry (1).wav")
sf.write('new_file.ogg',rate, sound)

print(sound)
print (rate)

framerate= wave_file.getframerate()
frames= wave_file.getnchannels()
width= wave_file.getsampwidth()

print("sampling rate: ", framerate, "Hz")
print("length: ", frames, "samples")
print("sample width: ", width, "bytes")

sound = 48000 # samples 
t=np.linspace(0, len(rate)/sound, len(sound), dytype=int)
plt.plot(t,sound)

'''data=[sound, rate]
t=np.zeros((rate, sound), dytpe=int)
w = np.fft.fft(np.sin(t))
ind_max = np.argmax(np.abs(w))
freq = data[ind_max]
freq_in_hertz = abs(freq * Fs)
t=np.linspace(0, len(y)/Fs, len(y)) #linspace is the fuction that will create the time vector
plt.plot(t,y)'''


#y = np.zeros(Fs)
#x1 = np.linspace(0, 10, Fs, endpoint=True)
#x2 = np.linspace(0, 10, Fs, endpoint=False)
#plt.plot(x1, y, 'o')

#plt.plot(x2, y + 0.5, 'o')

#plt.ylim([-0.5, 1])
#(-0.5, 1)
#plt.show()
# this code works 

'''Fs= 4800
T=1/Fs

x = linspace(0.0, Fs*T, Fs)
fftLength= length(data)
xdft= fft(data, fftLength)
maxAmp= max(a)
t = np.append(rate, sound)
sp = np.fft.fft(np.sin(t))
freq = np.fft.fftfreq(t.shape[-1])
plt.plot(freq, sp.real, freq, sp.imag)

plt.show()'''

'''w = np.fft.fft(np.sin(data)
freqs = np.fft.fftfreq(n, d=1./rate)

print(freqs.min(), freqs.max())'''


# Find the peak in the coefficients
    #find_max= index of first peaks in w

'''ind_max = np.argmax(np.abs(w))
freq = freqs[ind_max]
freq_in_hertz = abs(freq * framerate)'''


