import numpy as np
import scipy
from scipy import signal
import matplotlib as mpl
import csv
import time
import matplotlib.pyplot as plt
import _tkinter
import sys
fileName = sys.argv[1]


volts = []
times = []
#volts = numpy.empty(1,dtype = numpy.float32)
#times = numpy.empty(1,dtype = numpy.float32)
graphdata = open(fileName, 'r').read()
lines = graphdata.split('\n')
starttime = time.time()
for line in lines:
    if len(line)>1:
        x,y = line.split(',')
        times.append(float(x))
        volts.append(float(y))

#times = times[18000:25000]
#volts = volts[18000:25000]

timestep =[]
for i in range(len(times)-1):
    timestep.append(times[i+1] - times[i])
avgTstep = np.average(timestep)
print(avgTstep)
N = len(volts)
voltsFft = np.fft.fft(volts)
freqs = np.linspace(0,1/avgTstep,N)



samplingFreq = 1/avgTstep
nyq = 0.5 * samplingFreq
low = 14.0 / nyq
high = 14.1 / nyq
b, a = signal.butter(3, [low, high], btype='band')
filteredVoltsBand = signal.filtfilt(b,a,volts)
multiplied = np.multiply(volts,filteredVoltsBand)


cutoff = 0.5 / nyq
c, d = signal.butter(5, cutoff, 'low')

finalout = signal.filtfilt(c,d,multiplied)

lowpassOnly = finalout = signal.filtfilt(c,d,volts)

#filteredVoltsBand = signal.lfilter(b,a,volts)

filteredVoltsBandFft = np.fft.fft(filteredVoltsBand)
multFft = np.fft.fft(multiplied)
finalFFt = np.fft.fft(finalout)




plt.figure(1)
plt.subplot(211)
plt.ylabel('volts')
plt.xlabel('seconds')
plt.plot(times,volts)
plt.plot(times,filteredVoltsBand, 'r')
plt.plot(times,multiplied, 'k')
plt.plot(times, finalout, 'm')
plt.plot(times, lowpassOnly, 'c')

plt.subplot(212)
plt.xlabel('frequency (Hz)')
plt.plot(freqs[:N //2], np.abs(voltsFft)[:N//2]*1/N)
plt.plot(freqs[:N //2], np.abs(filteredVoltsBandFft)[:N//2]*1/N)
plt.plot(freqs[:N //2], np.abs(multFft)[:N//2]*1/N, 'k')
plt.plot(freqs[:N //2], np.abs(finalFFt)[:N//2]*1/N, 'm')
plt.show()
