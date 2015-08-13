import math
import numpy as np
import matplotlib.pyplot as plt



FREQ = 17
fields = 17
Y = [0.0]*fields
FUTURE = 6
# years... obviously
#xd = [1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013]
xd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
# original data
yd = [5560720, 5903032, 6307022, 6792396, 7103103, 7384053, 7765530, 8260017, 8794112, 9303993, 9750504, 10013647, 9846968, 10202191, 10689299, 11083148, 11484354]

# our projection of original data onto one dimension.
yl = [5644344.7058825493, 6014125.8014707565, 6383906.8970589638, 6753687.992647171, 7123469.0882354975, 7493250.1838237047, 7863031.279411912, 8232812.3750001192, 8602593.4705883265, 8972374.5661765337, 9342155.6617648602, 9711936.7573530674, 10081717.852941275, 10451498.948529482, 10821280.044117689, 11191061.139706016, 11560842.235294223]




diff = [0.0]*len(yd)
for index in range(len(yd)):
    #print "index ->", index
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


#def myFunction(i):
#    return -2128.07119605*i + 47289.11082529
    #return -2.12807120e+03*i + 8.54254933e+06


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



#kill the zero mode
#Y[0]=0
#for i in range(len(Y)):
#    Y[i] = 0

# Display graph

# next step is to find three highest frequency points tHF
# tHF = threeHighestFrequencies
tHF = [0.0,0.0,0.0,0.0]
Yone = 0.0
Ytwo = 0.0
Ythree = 0.0
Yfour = 0.0


# find the four highest frequencies in the transform.
# makes sure my FT is working
for i in range(1,len(f)-1):
    # save frequency if Y[i-1]<Y[i] and Y[i+1]<Y[i] (peaks)
    if(Y[i-1]<Y[i] and Y[i+1]<Y[i] and Y[i] > Yone):
        Yone = Y[i]
        tHF[0] = f[i]
        #print tHF[0]
    elif(Y[i-1]<Y[i] and Y[i+1]<Y[i] and Y[i] > Ytwo):
        if(tHF[1]<f[i]):
            tHF[1] = f[i]
            Ytwo = Y[i]
            #print tHF[1]
    elif(Y[i-1]<Y[i] and Y[i+1]<Y[i] and Y[i] > Ythree):
        if(tHF[2]<f[i]):
            Ythree = Y[i]
            tHF[2] = f[i]
            #print tHF[2]
    elif(Y[i-1]<Y[i] and Y[i+1]<Y[i] and Y[i] > Yfour):
        if(tHF[3]<f[i]):
            Yfour = Y[i]
            tHF[3] = f[i]
            #print tHF[3]

print tHF
print Yone,Ytwo,Ythree,Yfour

# Inverse Fourier Transform
# currently reconstructs the ORIGINAL GRAPH


### if we use Y, we compute power spectrum
### if we use the R_Points and I_Points, we get the Inverse Fourier Transform.
newY = [0.0]*fields
for i in range(fields):
    newY[i] = newY[i]/fields
    for k in range(fields):
    # R and I_Points held the data point 323 times the original
    #therefore I needed to multiply the points at that array index
    # by 1/fields, or the ratio of the number of points I have
        newY[i] = newY[i] + (float(I_Points[k])*1/fields)*math.sin((((2*math.pi*i)/1)*k)/fields)+(float(R_Points[k])*1/fields)*math.cos((((2*math.pi*i)/1)*k)/fields) # imaginary part  

print "our new function"

something = np.polyfit(xd,newY,1)
print something # where our frequencies are at 20 points


### 
def newPolyFitFnc(x):
    return something[0]*x+something[1]


newPolyValY = [0.0]*FUTURE
for i in range(FUTURE):
    newPolyValY[i] = newPolyFitFnc(i)

############################################################
####IFFT of cleaned difference minus original difference####
############################################################

newDiff = [0.0]*fields
for i in range(fields):
    newDiff[i] = newY[i] - diff[i]
    



### this loop computes the best fit line for the fourier transform we found using
### the difference between the real data points and the polynomial fit values.
dasX=[0.0]*FUTURE
for i in range(FUTURE):
    dasX[i] = i
dasY = [0.0]*FUTURE
for i in range(FUTURE): # next 28 
    dasY[i] = dasY[i]
    for k in range(FREQ): 
    # R and I_Points held the data point 323 times the original
    #therefore I needed to multiply the points at that array index
    # by 1/fields, or the ratio of the number of points I have
        dasY[i] = dasY[i] + ((float(R_Points[k])/FUTURE)*math.cos(2*math.pi*k/fields*i)) + ((float(I_Points[k])/FUTURE)*math.sin(2*math.pi*k/fields*i))


### finalY is the vector that holds the two best fit components.
### This will be our prediction.
finalY = [0.0]*FUTURE
for i in range(fields-1,FUTURE):
    finalY[i] = dasY[i] + yl[i]#oneMoreY[i] 
        
anX = [0.0]*FUTURE
for i in range(len(anX)):
    anX[i] = i

# variables to hold the outputs

### Try to get the coefficients straight from the polyfit fnc
### as opposed to hard-coding
### '''doesn't work'''
# function with the polyfit coefficients
def myFunction(x):
    return -2128.0711960*x + 47289.11082529

#oneMoreY holds the Y points of our polyfit function
oneMoreY = [0.0]*FUTURE
for i in range(FUTURE):
    oneMoreY[i] = myFunction(i)

# difference is the vector of the actual data points - our polyfit datapoints
#diff = [0.0]*fields
#for i in range(fields):
#    diff[i] = float(yd[i]) - float(oneMoreY[i])

#plt.plot(xd,newY)          #CLEANED IFT WITH 'FREQ' POINTS
#plt.plot(dasX,dasY)        # good thing to check out, our measure of stuff.
#plt.plot(anX,oneMoreY)    # this is the function polyfit
#plt.plot(anX,newPolyValY) # this is the IFFT diff polyfit
#plt.plot(xd,diff)  
#plt.plot(xd,newDiff)

#plt.plot(xd, yd)            # original data set.
#plt.plot(anX,finalY)      # this is our prediction
#plt.plot(xd, diff)
plt.plot(xd, Y)
plt.show()

