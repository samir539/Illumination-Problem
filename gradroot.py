import numpy as np
import math
from newton_raphson_system import*

def f(x):
    f = np.zeros(len(x))
    f[0] = (-30000*x[0])/((25+x[0]**2)**(5/2)) - (4500*(-40 + 2*x[0]))/(((x[1]**2 + (20-x[0])**2))**(5/2))
    f[1] = (3000)/((x[1]**2 + (20-x[0])**2)**(3/2)) + (-9000*x[1]**2)/((x[1]**2 + (20-x[0])**2)**(5/2))
    return f

x = np.array([6.0,6.0])  ##x[0] = x , x[1] = h2

print(newtonRaphson2(f,x))