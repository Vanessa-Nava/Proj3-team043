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
sf.write('new_file.wav',rate, sound)

print(sound)
print (rate)

framerate= wave_file.getframerate()
frames= wave_file.getnframes()
width= wave_file.getsampwidth()

print("sampling rate: ", framerate, "Hz")
print("length: ", frames, "samples")
print("sample width: ", width, "bytes")

Fs=4800
y = np.zeros(Fs)
x1 = np.linspace(0, 10, Fs, endpoint=True)
x2 = np.linspace(0, 10, Fs, endpoint=False)
plt.plot(x1, y, 'o')
plt.plot(x2, y + 0.5, 'o')

plt.ylim([-0.5, 1])
(-0.5, 1)
plt.show()
 

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



'''byteList = np.fromstring(wave_file.readframes(frames), dtype = np.int16)
byteList.astype(float)
maximum = max(byteList)
minimum = min(byteList)
highest_point =((abs(maximum) + abs(int(minimum))/2)
print("maximum occurs:", highest_point)'''


 
