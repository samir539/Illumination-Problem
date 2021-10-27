import numpy as np
from matplotlib import pyplot as plt
from matplotlib import lines
import math 
from bisection import bisection


#Parameter values
P1 = 2000           #Intensity of Lamp 1
P2 = 3000           #Intensity of Lamp 2
h1 = 5              #Height of Lamp 1
s = 20              #Distance between the lamps
vals = 2000         #no of points of evalutation
x = np.linspace(-20,30,vals)
h2hold = np.linspace(3,9,vals) #Height of Lamp 2, this is being varied
# print(h2hold)
X_min = np.array([])
a = 8
b = 11

def dC(x):
    return  (-3*P1*h1*x)/(h1**2 + x**2)**(5/2) - ((3/2)*P2*h2*(-2*s + 2*x))/(h2**2 + (s-x)**2)**(5/2)



for i in range(vals):
    h2 = h2hold[i]
    l = bisection(dC,a, b, tol = 1.0e-8)
    X_min = np.append(X_min,l )

# print (X_min)
plt.plot(h2hold,X_min, 'k')
plt.show()
    