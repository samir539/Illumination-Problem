import numpy as np
from matplotlib import pyplot as plt
from matplotlib import lines
import math 

#Parameter values
P1 = 2000           #Intensity of Lamp 1
P2 = 3000           #Intensity of Lamp 2
h1 = 5              #Height of Lamp 1
h2 = 6              #Height of Lamp 2
s = 20              #Distance between the lamps
vals = 2000         #no of points of evalutation
x = np.linspace(-20,30,vals)
pC = np.array([])   #Values of overall intensity
pDc = np.array([])  #Values of the derivative of the intensity 
pS1 = np.array([])  #Values of intensity for lamp 1 illumination ONLY
pS2 = np.array([])  #Values of intensity for lamp 2 illumination ONLY

# print (x)
# print(pC)


#We wish to plot C(x), C'(x), S1(x), S2(x) :
#Illumination, Derivative of Illumination, Illumination intensity by lamp 1 seperatly, Illumination intentisty by lamp 2 seperately
# C = (P1*h1)/(math.sqrt((h1**2 + x**2)**3)) + (P2*h2)/(math.sqrt((h2**2 + (s-x)**2)**3))

def C(x):
    result = (P1*h1)/(math.sqrt((h1**2 + x**2)**3)) + (P2*h2)/(math.sqrt((h2**2 + (s-x)**2)**3))
    return result

def dC(x):
    result = (-3*P1*h1*x)/(h1**2 + x**2)**(5/2) - ((3/2)*P2*h2*(-2*s + 2*x))/(h2**2 + (s-x)**2)**(5/2)
    return result

def S1(x):
    result = (P1*h1)/(math.sqrt((h1**2 + x**2)**3))
    return result

def S2(x):
    result = (P2*h2)/(math.sqrt((h2**2 + (s-x)**2)**3))
    return result

for i in range(vals):
   pC = np.append(pC, C(x[i]))
   pDc = np.append(pDc,dC(x[i]))
   pS1 = np.append(pS1,S1(x[i]))
   pS2 = np.append(pS2,S2(x[i]))


print(len(pC))
print(len(x))
plt.plot(x,pC,'r')
plt.plot(x,pDc, 'b--')
plt.plot(x,pS1, 'g',linestyle = 'dotted', alpha = 0.7)
plt.plot(x,pS2, 'y', linestyle = 'dotted', alpha = 0.7)
plt.axhline(y=0, color='k')
plt.show()
