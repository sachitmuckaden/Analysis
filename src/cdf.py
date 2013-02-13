import matplotlib
matplotlib.rcParams['backend'] = "Qt4Agg"

import matplotlib.pyplot as plt
import numpy as np

#xlabel = raw_input("Enter label for x-axis: ")
xlabel = "Latency (ms)"
#ylabel = raw_input("Enter label for y-axis: ")
ylabel = "CDF"
#filename = raw_input("Filename: ")
filename = "pingnetworkgoogle4Gus.txt"
outname = raw_input("Output filename: ")
titlename = outname
outname = "pingnetworkgoogleus4Gcdf" + outname
#title = raw_input("Title: ")
xcolumn = [1,2,3,4]
devicecolumn = int(raw_input("column: "))
filen = "/media/DATA/analysis/"+filename



count = 0
titles = ["Cumulative Distribution of Minimum Latency by Network -  "+titlename, "Cumulative Distribution of Maximum Latency by  "+titlename, "Cumulative Distribution of Average Latency by "+titlename+" on 4G", "Cumulative Distribution of Standard Deviation of Latency by Network -  "+titlename]
fig = plt.figure()
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages("./graphs/"+outname+".pdf")

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
        key = parts[devicecolumn-1]
        avg = float(parts[item-1])
        if avg>10000:
            avg = avg/100
            #print "Changed"
        
        if key in device_x:
            
            device_x[key].append(avg)
     
        else:
            device_x[key] =  [avg]
           
        
    #print device_x
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    
   
    
    for key in device_x.keys():
        if key=="          ":
            continue
        cx = device_x[key]
        #hist, bin_edges = np.histogram(cx, bins=np.arange(0,5010,10),  density=True)
        #plt.title(key)
        #print cx
        #print "Bin_egdes:" + str(len(bin_edges))
        #print "Histogram: " + str(len(hist))
        plt.hist(cx, bins=np.arange(0,400,0.5), normed = True, cumulative = True, histtype = 'step', label = key)
        #plt.plot(bin_edges,hist,'r-')
        #pp.savefig(fig)
    
    plt.title(titles[count])
    count = count + 1
    plt.legend(loc=4)
    #plt.show()
    #plt.plot()
    pp.savefig(fig)

pp.close()     
#fig.savefig("./graphs/"+outname+".png")