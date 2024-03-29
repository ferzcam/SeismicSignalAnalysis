import sys
import numpy as np
import matplotlib.pyplot as plt
import obspy
#from obspy.core import read
#from obspy.signal import freqattributes
from obspy.signal.freqattributes import bandwidth
#from obspy.signal.filter import bandpass

from pyrocko import util
from pyrocko.gui import marker as pm

from markers import lookPattern

if len(sys.argv) < 2:
    sys.exit("Filename was not introduced")

# set input file (which day to work on and which channel)
filename = sys.argv[1]
stream = obspy.read(filename)

trace = stream[0]

interval = 30 #seconds for window width
overlap = 15

tzero = trace.stats.starttime

traces = []

maxTime = 24*60*60-interval
#maxTime = 50 #for testing

fileToSave = open('data.txt', 'w')

for i in range(0, maxTime,overlap):
    auxTrace = trace.copy()
    cutData = auxTrace.trim(tzero+i,tzero+i+interval)
    np.savetxt(fileToSave, cutData.data ,newline=" ")
    fileToSave.write("\n")
fileToSave.close
