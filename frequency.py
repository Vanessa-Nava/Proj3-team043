import wave
import numpy as np
import scipy.io.wavfile
from struct import unpack

#channels=2, sampwidth=3, framerate=48000, nframes=816000, comptype=none,compname=not compressed

data_size = 4897156 #from previous code used to caluclate the size
fname = "iCry.wav"

wav_file = wave.open(fname, 'rb')
print (wav_file.getparams())

frate = wav_file.getframerate()
nframes = wav_file.getnframes()
read_frames = wav_file.readframes(nframes)


#data=wav_file.getframerate()
#data= frate
d = 816000 * data_size

#data =wav_file.readframes(data_size)
wav_file.close()

data = unpack("%i" %  2 * nframes, read_frames)

#bytearray(wav_file.read(8)) 

data= np.array(data)
#sound is now in a list format with values

w = np.fft.fft(data)
freqs = np.fft.fftfreq(len(w))
print(freqs.min(), freqs.max())


    # Find the peak in the coefficients
    
#ind_max= index of first peaks in w
ind_max = np.argmax(np.abs(w))
freq = freqs[ind_max]
freq_in_hertz = abs(freq * frate)

print(freq_in_hertz)




#icry has 2 nchannels
# 3 - samplewidth
# 48000 framerate
# 816000 nframes

'''chunk = 500
wav = wave.open('iCry.wav')

rate = wav.getframerate() #48000
wavWidth = wav.getsampwidth();
data = scipy.io.wavfile.read('iCry.wav')



sin = np.sin(data)
#print wav.readframes(chunk)'''







'''import numpy as np
from scipy.io.wavfile import write

# samples per second
fs = 44100

# frequency of the sine wave, Concert C
freq_hz = 260.0

# duration
duration_s = 5.0

sample_nums = np.arange(duration_s * fs)

waveform = np.sin(2 * np.pi * sample_nums * freq_hz / fs)

waveform_quiet = waveform * 0.3

waveform_integers = np.int16(waveform_quiet * 32767)

write('first_sine_wave.wav', fs, waveform_integers)







def freq_from_fft(signal, fs):
    """Estimate frequency from peak of FFT
    Pros: Accurate, usually even more so than zero crossing counter
    (1000.000004 Hz for 1000 Hz, for instance).  Due to parabolic
    interpolation being a very good fit for windowed log FFT peaks?
    https://ccrma.stanford.edu/~jos/sasp/Quadratic_Interpolation_Spectral_Peaks.html
    Accuracy also increases with signal length
    Cons: Doesn't find the right value if harmonics are stronger than
    fundamental, which is common.
    """
    N = len(signal)

    # Compute Fourier transform of windowed signal
    windowed = signal * kaiser(N, 100)
    f = rfft(windowed)
    # Find the peak and interpolate to get a more accurate peak
    i_peak = argmax(abs(f))  # Just use this value for less-accurate result
    i_interp = parabolic(log(abs(f)), i_peak)[0]

    # Convert to equivalent frequency
    return fs * i_interp / N  # Hz
'''