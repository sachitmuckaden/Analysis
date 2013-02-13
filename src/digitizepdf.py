import matplotlib
matplotlib.rcParams['backend'] = "Qt4Agg"

import matplotlib.pyplot as plt
import numpy as np
from numpy import  linspace
from scipy.interpolate import spline

#xlabel = raw_input("Enter label for x-axis: ")
xlabel = "Latency (ms)"
#ylabel = raw_input("Enter label for y-axis: ")
ylabel = "PDF"
#filename = raw_input("Filename: ")
filename = "pingbatterygoogleus3G.txt"
outname = raw_input("Output filename: ")
titlename = outname
outname = "pingbatterygoogleus3Gpdf" + outname
#title = raw_input("Title: ")
xcolumn = [1,2,3,4]
devicecolumn = int(raw_input("column: "))
filen = "/media/DATA/analysis/"+filename



count = 0
titles = ["Minimum Latency by Battery level", "Maximum Latency by Battery Level", "Median values of Latency by battery level", "Median values of Standard Deviation over 5 pings by Battery level"]
fig = plt.figure()
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages("./graphs/"+outname+".pdf")

#bins = [0,50,101]
bins = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,101]
#bins = np.arange(0,105,5)
print bins
for item in xcolumn:
    f = open(filen)
    cx = []
    parts = []
    device_x = {}
    
    plt.cla()
    print item
    print device_x
    for line in f:
        parts = line.split('|')
        k = int(parts[devicecolumn-1])
        #print ktmp
        #local = ktmp.split(" ")
        #time = local[2]
        #print time
        #hr = time.split(":")
        #print hr
        #k = int(hr[0])
        #print k
        if k > 100 or k<0:
            continue
        #print k
        node = []
        node = np.digitize(np.array([k]), bins)
        avg = float(parts[item-1])
        if avg>10000:
            avg = avg/100
        key = node[0]
       
        #print key
        if key in device_x:
            
            device_x[key].append(avg)
     
        else:
            device_x[key] =  [avg]
           
        
    #print device_x
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    
    data = []
    for keyt in device_x.keys():
        cx = device_x[keyt]
        #print cx
        data.append(cx)
        #hist, bin_edges = np.histogram(cx, bins=np.arange(0,500,5),  density=True)
        #print len(hist)
        #print len(bin_edges)
        #hist = np.append(hist, 0)
        #plt.title(key)
        #print cx
        #print "Bin_egdes:" + str(len(bin_edges))
        #print "Histogram: " + str(len(hist))
        #xnew = linspace(bin_edges.min(), bin_edges.max(),500 )
        #print len(hist)
        #print len(bin_edges)
        #ysmooth = spline (bin_edges, hist, xnew )
        #print device_x[keyt]
        #plt.plot(xnew, ysmooth,  label = str(bins[keyt-1])+" - "+str(bins[keyt]))
        #print keyt
        #plt.hist(cx, bins=np.arange(0,300,1), normed = True, cumulative = False, histtype = 'step', align = 'mid', label = str(bins[keyt-1])+" - "+str(bins[keyt]))
        #plt.plot(bin_edges,hist,'r-')
        #pp.savefig(fig)
    
    plt.boxplot(data,0,'')
    plt.title(titles[count])
    count = count + 1
    plt.legend()
    #plt.show()
    #plt.plot()
    pp.savefig(fig)

pp.close()    