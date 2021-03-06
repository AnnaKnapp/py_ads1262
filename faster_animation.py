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

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graphdata = open(fileName, 'r').read()
    lines = graphdata.split('\n')
    xs=[]
    ys=[]
    for i in range(1,600):
        line = lines[i*-1]
        if len(line) > 19:
            x,y = line.split(',')
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs,ys)

ani = animation.FuncAnimation(fig, animate, interval = 1)
plt.show()
