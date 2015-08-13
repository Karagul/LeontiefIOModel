import math
import numpy as np
import matplotlib.pyplot as plt

FREQ = 17
fields = 17
Y = [0.0]*fields
xd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
#xd = [1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013]
yd = [5560720, 5903032, 6307022, 6792396, 7103103, 7384053, 7765530, 8260017, 8794112, 9303993, 9750504, 10013647, 9846968, 10202191, 10689299, 11083148, 11484354]

# make the scatter plot
plt.scatter(xd, yd, s=30, alpha=0.15, marker='o')

# determine best fit line
par = np.polyfit(xd, yd, 1, full=True)

slope=par[0][0]
intercept=par[0][1]
xl = [min(xd), max(xd)]
yl = [slope*xx + intercept for xx in xd] #was xl
print "yl vals --> ", yl
#yl = [par[0]*x + par[1] for x in xd]

"""
diff = [0.0]*len(yd)
for index in range(len(yd)):
    print "index ->", index
    diff[index] = yd[index] - yl[index]


# Real Fourier part
def FourierR(Array):
    # yields the real component of the Fourier Transform
    toReturn = [0.0]*fields
    for k in range(FREQ):
        for j in range(len(Array)):
            toReturn[k] = toReturn[k]+(float(Array[j]))*math.cos((2*math.pi*j*k)/fields)
            
    return toReturn

# yields the imaginary component of the Fourier Transform
def FourierI(Array):
    IReturn = [0.0]*fields
    for k in range(FREQ):
        for j in range(len(Array)):
            IReturn[k] = IReturn[k]+(float(Array[j]))*math.sin((2*math.pi*j*k)/fields)
    return IReturn



# vectors to hold the transform data
R_Points = FourierR(diff)
I_Points = FourierI(diff)


#Power Spectrum

for i in range(fields):
    Y[i] = R_Points[i]*R_Points[i] + I_Points[i]*I_Points[i]

# next we will calculate the frequency
# each point Y[k] has an associated frequency f[k] = (k-1)/tau*N
tau=1.0   #time unit (1 month)
f = [0.0]*fields
for i in range(fields/2):
    f[i] = i/(fields*tau)

"""

## Print stuff
#plt.scatter(xd, mydiff, alpha=1.0, marker='x')
# coefficient of determination, plot text
variance = np.var(yd)
residuals = np.var([(slope*xx + intercept - yy) for xx,yy in zip(xd, yd)])
Rsqr = np.round(1-residuals/variance, decimals=2)
plt.text(.9*max(xd)+.1*min(xd),.9*max(yd)+.1*min(yd),'$R^2 = %0.2f$'% Rsqr, fontsize=20)

plt.xlabel("Time (Years)")
plt.ylabel("Personal Consumption (MM of dollars)")

yerr = [abs(slope*xx + intercept - yy) for xx,yy in zip(xd,yd)]
par = np.polyfit(xd, yerr, 2, full=True)

yerrUpper = [(xx*slope+intercept)+(par[0][0]*xx**2 + par[0][1]*xx + par[0][2]) for xx,yy in zip(xd,yd)]
yerrLower = [(xx*slope+intercept)-(par[0][0]*xx**2 + par[0][1]*xx + par[0][2]) for xx,yy in zip(xd,yd)]

print("par[0]:{}, par[1]:{}".format(par[0], par[1]))

#plt.plot(xd, Y)
#plt.plot(xl, yl, '-r')
plt.plot(xd, yl, '-r')
plt.plot(xd, yerrLower, '--r')
plt.plot(xd, yerrUpper, '--r')
plt.show()
