import numpy as np
from numpy import sign
import math 
import error

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

def bisection(f,x1,x2,switch=1,tol=1.0e-9):
    f1 = f(x1)
    if f1 == 0.0:
        return x1
    f2 = f(x2)
    if f2 == 0.0:
        return x2
    if  sign(f1) == sign(f2):
        error.err('Root is not bracketed')
    n = int(math.ceil(math.log(abs(x2-x1)/tol)/math.log(2.0)))

    for i in range(n):
        x3 = 0.5 * (x1 + x2)
        f3 = f(x3)
        if (switch == 1) and (abs(f3) > abs(f1))  and (abs(f3) > abs(f2)):
            return None
        if f3 == 0.0:
            return x3
        if sign(f2) != sign(f3):
            x1 = x3
            f1 = f3
        else:
            x2 = x3 
            f2 = f3
        
    return (x1 + x2)/2.0

def dC(x):
    return (-3*P1*h1*x)/(h1**2 + x**2)**(5/2) - ((3/2)*P2*h2*(-2*s + 2*x))/(h2**2 + (s-x)**2)**(5/2)

# def ourFunc(x):
#     return x**3 - 10*x**2 + 5 
a = 8
b = 11

l = bisection(dC, a, b, tol = 1.0e-8)
print('l=', '{:6.9f}'.format(l))
