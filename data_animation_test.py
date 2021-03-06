import numpy
import scipy
from scipy import signal
import matplotlib as mpl
import csv
import time
import matplotlib.pyplot as plt
import _tkinter
import matplotlib.animation as animation
from matplotlib import style
import sys

fileName = sys.argv[1] + '.txt'

#volts = numpy.empty(1,dtype = numpy.float32)
#times = numpy.empty(1,dtype = numpy.float32)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graphdata = open(fileName, 'r').read()
    lines = graphdata.split('\n')
    xs=[]
    ys=[]
    for line in lines:
        if len(line) > 1:
            x,y = line.split(',')
            xs.append(x)
            ys.append(y)
    if len(xs) >= 1000:    #uncomment these 3 lines to have the graph move and only show 100 pts at a time
        xs = xs[-1000:-1]
        ys = ys[-1000:-1]
    ax1.clear()
    ax1.plot(xs,ys)

ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.show()
