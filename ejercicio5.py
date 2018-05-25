# Ejercicio5
# Resuelva el siguiente sistema acoplado de ecuaciones diferenciales 
# dx/dt = sigma * (y - x)
# dy/dt = rho * x - y -x*z
# dz/dt = -beta * z + x * y
# con sigma = 10, beta=2.67, rho=28.0,
# condiciones iniciales t=0, x=0.0, y=0.0, z=0.0, hasta t=5.0.
# Prepare dos graficas con la solucion: de x vs y (xy.png), x vs. z (xz.png) 

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def dx(x,y,z):
    sigma=10.0
    return sigma*(y-x)

def dy(x,y,z):
    rho=28.0
    return rho * x - y -x*z
    
def dz(x,y,z):
    beta=2.67
    return -beta * z + x * y

t_in=0.0
t_fin=5.0


n=1000
dt=t_fin/n
x=np.zeros(n)
y=np.zeros(n)
z=np.zeros(n)
for i in range(1,n):
    
    x[i]=x[i-1]+(dt*dx(x[i-1],y[i-1],z[i-1]))
    y[i]=y[i-1]+(dt*dy(x[i-1],y[i-1],z[i-1]))
    z[i]=z[i-1]+(dt*dz(x[i-1],y[i-1],z[i-1]))
    
plt.scatter(y,x)
plt.xlabel("y")
plt.ylabel("x")
plt.title("xy")
plt.savefig("xy.png")

plt.clf()

plt.scatter(z,x)
plt.xlabel("z")
plt.ylabel("x")
plt.title("xz")
plt.savefig("xz.png")





