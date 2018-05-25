# Ejercicio 2
# Complete el siguiente codigo para recorrer la lista `x` e imprima
# los numeros impares y que pare de imprimir al encontrar un numero mayor a 800
import numpy as np

x = np.int_(np.random.random(100)*1000)
i=0
j=i
while(i<800 and j<100):
    if(x[j]%2!=0):
        i=x[j]
        print(x[j])
    j=j+1

