import math
import numpy as np
import matplotlib.pyplot as plt

FREQ = 17
fields = 17
Y = [0.0]*fields
#xd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
xd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
#xdates = [1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013]
xdates = [1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012]
#xd = [1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013]

#yd = [5560720, 5903032, 6307022, 6792396, 7103103, 7384053, 7765530, 8260017, 8794112, 9303993, 9750504, 10013647, 9846968, 10202191, 10689299, 11083148, 11484354]
yd = [5560720, 5903032, 6307022, 6792396, 7103103, 7384053, 7765530, 8260017, 8794112, 9303993, 9750504, 10013647, 9846968, 10202191, 10689299, 11083148]

# make the scatter plot
plt.scatter(xdates, yd, s=30, alpha=0.3, marker='o')

# determine best fit line
par = np.polyfit(xd, yd, 1, full=True)
#xd.append(18)
#xdates.append(2014)
slope=par[0][0]
intercept=par[0][1]
xl = [min(xd), max(xd)]
print "slope: {0}, intercept: {1}".format(slope, intercept)
best_fit = [slope*xx + intercept for xx in xd] #was xl
yd.append(slope*17 + intercept)
print "predicted amount --> {}".format(yd[16])
plt.scatter(2013,yd[16], s=30, alpha=0.8, marker='x')
print "best_fit vals --> ", best_fit
#best_fit = [par[0]*x + par[1] for x in xd]

"""
deltaYoY = [0.0]*(len(yd)-1)
for index in range(len(yd)):
    if(index is not 0):
        deltaYoY[index-1] = ((float(yd[index]) - float(yd[index-1]))/float(yd[index-1]))*100
        
print "Delta's -->{0}".format(deltaYoY)  
fourierTransform = np.fft.fft(deltaYoY)
print "Fourier Transform --> {0}".format(fourierTransform)


data = deltaYoY
print len(data)
ps = np.abs(np.fft.fft(data))**2

time_step = float(1 / float(len(yd)))
print time_step
freqs = np.fft.fftfreq(len(data), time_step)
idx = np.argsort(freqs)
print max(freqs)
plt.plot(freqs[idx], ps[idx])
"""

# coefficient of determination, plot text
variance = np.var(yd)
residuals = np.var([(slope*xx + intercept - yy) for xx,yy in zip(xd, yd)]) #residual sum of squares
Rsqr = np.round(1-residuals/variance, decimals=2)
plt.text(.9*max(xd)+.1*min(xd),.9*max(yd)+.1*min(yd),'$R^2 = %0.2f$'% Rsqr, fontsize=20)

plt.xlabel("Time (Years)")
#plt.best_fitabel("Personal Consumption (MM of dollars)")
plt.ylabel("Percent Change (YoY) Personal Consumption")

yerr = [abs(slope*xx + intercept - yy) for xx,yy in zip(xd,yd)]
par = np.polyfit(xd, yerr, 2, full=True)

yerrUpper = [(xx*slope+intercept)+(par[0][0]*xx**2 + par[0][1]*xx + par[0][2]) for xx,yy in zip(xd,yd)]
yerrLower = [(xx*slope+intercept)-(par[0][0]*xx**2 + par[0][1]*xx + par[0][2]) for xx,yy in zip(xd,yd)]

print("par[0]:{}, par[1]:{}".format(par[0], par[1]))

#plt.plot(xd, Y)
#plt.plot(xl, best_fit, '-r')

plt.plot(xdates, best_fit, '-r')
#plt.plot(xd, deltaYoY, '-r')
plt.plot(xdates, yerrLower, '--r')
plt.plot(xdates, yerrUpper, '--r')
plt.show()
