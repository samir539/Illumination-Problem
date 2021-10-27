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
h2 = np.linspace(3,9,vals) #Height of Lamp 2, this is being varied
pC = np.zeros((1,2000))   #Values of overall intensity
pChold = np.zeros((1,2000))


def C(x, h2):
    return (P1*h1)/(math.sqrt((h1**2 + x**2)**3)) + (P2*h2)/(math.sqrt((h2**2 + (s-x)**2)**3))
C2 = np.vectorize(C)
X, Y = np.meshgrid(x,h2)
# print(len(X))
# print(len(Y))
Z = C2(X, Y)


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contourf(X, Y, Z, 50)
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
#                 cmap='viridis', edgecolor='none')
# ax.plot_trisurf(X,Y,Z,linewidth = 0.2, antialiased=True)
# ax.plot_surface(X,Y,Z, rstride=1, cstride =1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()








# for j in range(vals):
#     pC = np.vstack([pC,pChold])
#     # for i in range(vals):
#     #     pChold = np.append(pChold, C(x[j],h2[i]))
# print(len(pC))
# print(pC)



# X, Y = np.meshgrid(x,h2)

