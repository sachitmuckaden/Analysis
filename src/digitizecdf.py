import matplotlib
matplotlib.rcParams['backend'] = "Qt4Agg"

import matplotlib.pyplot as plt
import numpy as np


#xlabel = raw_input("Enter label for x-axis: ")
xlabel = "Latency (ms)"
#ylabel = raw_input("Enter label for y-axis: ")
ylabel = "CDF"
#filename = raw_input("Filename: ")
filename = "pingbatteryatlantaus3G.txt"
outname = raw_input("Output filename: ")
titlename = outname
outname = "pingbatteryatlantaus3Gcdf" + outname
#title = raw_input("Title: ")
xcolumn = [1,2,3,4]
devicecolumn = int(raw_input("column: "))
filen = "/media/DATA/analysis/"+filename



count = 0
titles = ["Cumulative Distribution of Minimum Latency by Battery "+titlename, "Cumulative Distribution of Maximum Latency by Battery "+titlename, "Cumulative Distribution of Average Latency by Battery "+titlename, "Cumulative Distribution of Standard Deviation of Latency by Battery "+titlename]
fig = plt.figure()
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages("./graphs/"+outname+".pdf")

bins = [0,25,50,75,101]
#bins = np.arange(0,125,8)
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
        #if k > 31 or k<0:
            #continue
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
    
    
   
   
    for keyt in device_x.keys():
        cx = device_x[keyt]
        
        #hist, bin_edges = np.histogram(cx, bins=np.arange(0,300,5),  density=True)
        #print len(hist)
        #print len(bin_edges)
        #hist = np.append(hist, 0)
        #plt.title(key)
        #print cx
        #print "Bin_egdes:" + str(len(bin_edges))
        #print "Histogram: " + str(len(hist))
        #xnew = linspace(bin_edges.min(), bin_edges.max(),300 )
        #print len(hist)
        #print len(bin_edges)
        #ysmooth = spline (bin_edges, hist, xnew )
        #plt.plot(xnew, ysmooth)
        #print keyt
        plt.hist(cx, bins=np.arange(0,500,1), normed = True, cumulative = True, histtype = 'step', align = 'mid', label = str(bins[keyt-1])+" - "+str(bins[keyt]))
        #plt.plot(bin_edges,hist,'r-')
        #pp.savefig(fig)
    
    plt.title(titles[count])
    count = count + 1
    plt.legend(loc = 4)
    #plt.show()
    #plt.plot()
    pp.savefig(fig)

pp.close()     
#fig.savefig("./graphs/"+outname+".png")