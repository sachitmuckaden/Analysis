import matplotlib
matplotlib.rcParams['backend'] = "Qt4Agg"

import matplotlib.pyplot as plt
import numpy as np
from numpy import  linspace
from scipy.interpolate import spline

#xlabel = raw_input("Enter label for x-axis: ")
xlabel = "Hour of the day"
#ylabel = raw_input("Enter label for y-axis: ")
ylabel = "Ping times (ms)"
#filename = raw_input("Filename: ")
filename = "pingtimegoogleus.txt"
outname = raw_input("Output filename: ")
titlename = outname
#title = raw_input("Title: ")
outname = "pingtimegoogleuspdf" + outname
xcolumn = [1,2,3,4]
devicecolumn = int(raw_input("column: "))
filen = "/media/DATA/analysis/"+filename



count = 0
titles = ["Minimum Latency by Hour of the day", "Maximum Latency by Hour of the day", "Median values of Latency by Hour of the day", "Median values of Standard deviation over 5 pings by Hour of the day"]
fig = plt.figure()
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages("./graphs/"+outname+".pdf")
ss = np.arange(0,25,1)
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
        ktmp = parts[devicecolumn-1]
        local = ktmp.split(" ")
        time = local[2]
        #print time
        hr = time.split(":")
        #print hr
        key = int(hr[0])
        #print k
        avg = float(parts[item-1])
        if avg>10000:
            avg = avg/100
            #print "Changed"
        if key<0 or key>31:
                continue
        if key in device_x:
            
            device_x[key].append(avg)
     
        else:
            device_x[key] =  [avg]
           
        
    #print device_x
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    
    
    print device_x.keys()
    med = []
    err=[]
    data=[]
    for key in device_x.keys():
        print key
        if key == "          ":
            continue
        cx = device_x[key]
        #data.append(cx)
        #print key
        med.append(np.median(cx)) 
        #err.append(np.std(cx))
        #hist, bin_edges = np.histogram(cx, bins=np.arange(0,300,10),  density=True)
        #print len(hist)
        #print len(bin_edges)
        #hist = np.append(hist, 0)
        #plt.title(key)
        #print cx
        #print "Bin_egdes:" + str(len(bin_edges))
        #print "Histogram: " + str(len(hist))
        #xnew = linspace(bin_edges.min(), bin_edges.max(),400 )
        #print len(hist)
        #print len(bin_edges)
        #ysmooth = spline (bin_edges, hist, xnew )
        #ymod = ysmooth[ysmooth>=0]
        
        #print keyt
        #plt.hist(cx, bins=np.arange(0,300,1), normed = True, Probability = False, histtype = 'step', align = 'mid', label = str(bins[keyt-1])+" - "+str(bins[keyt]))
        #plt.plot(bin_edges,hist,'r-')
        #pp.savefig(fig)
    #print med    
    #plt.boxplot(data,0,'')
    plt.plot(device_x.keys(),med,'ro')
    plt.plot(device_x.keys(),med,'r-')
    #plt.errorbar(device_x.keys(), med, err)
    #plt.legend(('1- GSM', '2- CDMA'), loc = 2)
    plt.title(titles[count])
        
    count = count + 1
    #plt.legend()
    #plt.show()
    #plt.plot()
    pp.savefig(fig)

pp.close()     
#fig.savefig("./graphs/"+outname+".png")
