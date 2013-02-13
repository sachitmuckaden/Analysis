import matplotlib
matplotlib.rcParams['backend'] = "Qt4Agg"

import matplotlib.pyplot as plt
#import numpy as np

xlabel = raw_input("Enter label for x-axis: ")
ylabel = raw_input("Enter label for y-axis: ")
xranges = int(raw_input("Enter xrange (start): "))
xranget = int(raw_input("Enter xrange (end): "))
yranges = int(raw_input("Enter xrange (start): "))
yranget = int(raw_input("Enter xrange (end): "))
title = raw_input("Graph title: ")
filename = raw_input("Filename: ")
outname = raw_input("Output filename: ")
xcolumn = int(raw_input("X-Column: "))
ycolumn = int(raw_input("Y-Column: "))

filen = "/media/DATA/analysis/"+filename

f = open(filen)
cx = []
cy = []

for line in f:
    parts = line.split('|')
    cx.append(parts[xcolumn-1])
    cy.append(parts[ycolumn-1])
    
fig = plt.figure()
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.axis([xranges,xranget, yranges, yranget])
plt.title(title)
plt.plot(cx,cy,'rx')
fig.savefig("./graphs/"+outname+".png")

