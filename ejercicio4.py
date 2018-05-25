#Ejercicio4
# 'y' es una senal en funcion del tiempo 't' con las unidades descritas en el codigo.

# a. Grafique la senal en funcion del tiempo en la figura 'senal.png' ('y' vs. 't')
# b. Calule la transformada de Fourier (sin utilizar funciones de fast fourier transform) y
# grafique la norma de la transformada en funcion de la frecuencia (figura 'fourier.png')
# c. Lleve a cero los coeficientes de Fourier con frecuencias mayores que 10000 Hz y calcule 
# la transformada inversa para graficar la nueva senal (figura 'filtro.png')

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


n = 512 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 128 ) #128 samples per frequency
t = np.linspace( 0, (n-1)*dt, n) 
y = np.sin(2 * np.pi * f * t) + np.cos(2 * np.pi * f * t * t)
noise = 1.4*(np.random.rand(n)+0.7)
y  =  y + noise

plt.plot(t,y)
plt.xlabel("tiempo")
plt.ylabel("senal")
plt.title("Senal")
plt.savefig("senal.png")

tran=np.zeros(n, dtype="complex")
freq=np.ones(n)
a=np.ones(n,dtype="complex")

for i in range(n):
    for k in range(len(y)):
        tran[i]+=y[k]*np.exp(-2j*np.pi*i*k/n)
    if(np.angle(tran[i])==0):
        freq[i]=-5
    else:
        freq[i]=2*np.pi/np.angle(tran[i])

tran=tran/n
plt.clf()

plt.plot(freq,abs(tran))
plt.savefig("fourier.png")

tran=np.where(abs(freq)>1000,0,tran)

new_y=np.zeros(n, dtype="complex")

for i in range(n):
    for k in range(len(y)):
        new_y[i]+=tran[k]*np.exp(2j*np.pi*i*k/n)

plt.clf()
plt.plot(t,abs(new_y))
plt.savefig("filtro.png")