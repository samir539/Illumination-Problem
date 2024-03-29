import numpy as np
from gaussPivot import*
import math
##function looks to find the roots or f(x) = 0
## f is a vector of functions
## x is a vector of variables


def newtonRaphson2(f,x,tol=1.0e-9):

    def jacobian(f,x):
        h = 1.0e-4
        n = len(x)
        jac = np.zeros((n,n))
        f0 = f(x)
        for i in range(n):
            temp = x[i]
            x[i] = temp + h
            f1 = f(x)
            x[i] = temp
            jac[:,i] = (f1-f0)/h
        return jac,f0
    
    for i in range(30):
        jac,f0 = jacobian(f,x)
        if math.sqrt(np.dot(f0,f0)/len(x)) < tol: return x
        dx = gaussPivot(jac, -f0)
        x = x + dx
        if math.sqrt(np.dot(dx,dx)) < tol * max(max(abs(x)),1.0):
            return x
        
    print("too many iterations")