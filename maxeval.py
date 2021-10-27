import math
from matplotlib import pyplot as plt
from bisection import bisection
import numpy as np
import error
from numpy import sign

import sys
def err(string):
    print(string)
    input('Press something to exit')
    sys.exit()
#we still use the same constant values for all the constants
P1 = 2000           #Intensity of Lamp 1
P2 = 3000           #Intensity of Lamp 2
h1 = 5              #Height of Lamp 1
s = 20              #Distance between the lamps
vals = 2000         #no of points of evalutation
x = np.linspace(-20,30,vals)
h2 = np.linspace(3,9,vals) #Height of Lamp 2, this is being varied

#we wish to find the maximally illuminated points of C(x,h2)
#To achieve this we find the gradient of C(x,h2) and the use bisection to find the values of x and h2 where the maximum occurs (i.e. where the root is)

#Expression for grad(C(x,h2))

#i comp
def GradCx(x): 
    return (-3*P1*h1*x)/(h1**2 + x**2)**(5/2) - ((3/2)*P2*h2*(-2*s+2*x))/(h2**2+(s-x**2))**(5/2)


#j comp
def GradCh2(h2): 
    return (P2)/(h2**2+(s-x)**2)**(3/2) + (P2*h2*(-3/2)*2*h2)/(h2**2+(s-x)**2)**(5/2)  

      
# intervals of bisection
a = 6
b = 10

#bisection function
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



#carrying out the bisection
i = bisection(GradCx, a, b, tol = 1.0e-8)
print('l=', '{:6.9f}'.format(i))

j = bisection(GradCh2, a, b, tol = 1.0e-8)
print('l=', '{:6.9f}'.format(j))

