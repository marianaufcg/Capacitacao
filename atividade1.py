import matplotlib.pyplot as plt
import numpy as np

# Solução analíica

xa = np.arange(0, 10, 0.001)

def y(x):
    aux = np.sin(np.pi * x) - (np.pi * np.cos(np.pi * x))
    r = (aux/(1 + np.power(np.pi, 2))) + np.exp(-x)  + (np.pi * np.exp(-x))/(1 + np.power(np.pi, 2))
    return r

# Solução numérica pelo método das diferenças finitas

def ylinha(x, y):
    return (np.sin(np.pi * x) - y)

def pontos(h):

    xn = np.arange(0, 10+h, h)

    yn = np.zeros(len(xn))
    yn[0] = 1

    # Primeira iteração pelo método progressivo

    y1 = ylinha(0, 1)*h + 1
    yn[1] = y1

    # Iterações seguintes pelo método central

    for i in range(1, len(xn)-1, 1):
        yn[i+1] = 2*h*ylinha(xn[i], yn[i]) + yn[i-1]

    return xn, yn

xn, yn = pontos(0.0001)

# Plotagem dos gráficos

plt.figure(figsize=(8, 6))
plt.plot(xa, y(xa), label='solução analítica', color='red')
plt.plot(xn, yn, label='solução numérica', color= 'blue')
plt.xlabel('x')
plt.ylabel('y')
plt.legend() 
plt.grid(True) 
plt.show()
