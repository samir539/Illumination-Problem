import numpy as np
import math
from numpy import sign
import error

def ridder(f,a,b,tol=1.0e-9):
    fa = f(a)
    if fa == 0.0:
        return a
    fb = f(b)
    if fb == 0.0:
        return b
    f2 = f(x2)
    if sign(f2) != sign(f3):
        x1 = x3
        f1 = f3
    for i in range(30):
        c = 0.5 * (a+b)
        fc = f(c)
        s = math.sqrt(fc**2 - fa*fb)
        if s == 0.0:
            return None
        dx = (c-a)*fc/s
        if (fa - fb) < 0.0:
            dx = -dx
        x = c + dx
        fx = f(x)
    #testing for convergence
        if i > 0:
            if abs(x-  xOld) < tol*max(abs(x), 1.0):
                return x
            xOld = x
        #Rebracketing the root as tightly as possible
        if sign(fc) == sign(fx):
            if sign(fa) != sign(fx):
                b = x 
                fb = fx
            else:
                a=x
                fa = fx
        else:
            a = c
            b = x
            fa = fc 
            fb = fx
    return None
    print("too many iterations")



def ourFunc(x):
    return x**3 - 10*x**2 + 5 
a = 0.6
b = 0.8

print(ridder(ourFunc,a,b))