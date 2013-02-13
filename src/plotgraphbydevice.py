import matplotlib
matplotlib.rcParams['backend'] = "Qt4Agg"

import matplotlib.pyplot as plt
#import numpy as np

xlabel = raw_input("Enter label for x-axis: ")
ylabel = raw_input("Enter label for y-axis: ")
xranges = int(raw_input("Enter xrange (start): "))
xranget = int(raw_input("Enter xrange (end): "))
yranges = int(raw_input("Enter yrange (start): "))
yranget = int(raw_input("Enter yrange (end): "))
title = raw_input("Graph title: ")
filename = raw_input("Filename: ")
outname = raw_input("Output filename: ")
xcolumn = int(raw_input("X-Column: "))
ycolumn = int(raw_input("Y-Column: "))
devicecolumn = int(raw_input("column: "))
filen = "/media/DATA/analysis/"+filename

f = open(filen)
cx = []
cy = []
device_x = {}
device_y = {}
count = 1
for line in f:
    parts = line.split('|')
    key = parts[devicecolumn-1]
    if key in device_x:
        device_x[key].append(parts[xcolumn-1])
        device_y[key].append(parts[ycolumn-1])
    else:
        device_x[key] =  [parts[xcolumn-1]]
        device_y[key] = [parts[ycolumn-1]]
    
fig = plt.figure()
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.axis([xranges,xranget, yranges, yranget])
plt.title(title)

from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages("./graphs/"+outname+".pdf")

for key in device_x.keys():
    cx = device_x[key]
    cy = device_y[key]
    plt.plot(cx,cy,'rx')
    pp.savefig(fig)

pp.close()     
#fig.savefig("./graphs/"+outname+".png")