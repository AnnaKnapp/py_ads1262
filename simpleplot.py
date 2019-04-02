import numpy
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

timestep = []
for i in range(len(times)-1):
    timestep.append(times[i+1] - times[i])
avgTstep = numpy.average(timestep)
print(avgTstep)


plt.figure(1)
plt.subplot(211)
plt.ylabel('volts')
plt.xlabel('seconds')
plt.plot(times,volts, 'r')
plt.show()
