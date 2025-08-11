import numpy as np
import matplotlib.pyplot as plt

# ~~~~~~~~~~~~~~~~~~~
# Soluções Analíticas
# ~~~~~~~~~~~~~~~~~~~

x = np.linspace(0, 10, 100)

def solucao1(x):
    return ((7/3)*np.exp(-x) - (4/3)*np.exp(-4*x))

def solucao2(x):
    return (np.exp(-2*x) +5*x*np.exp(-2*x))

def solucao3(x):
    return (np.exp(-2*x)*(np.cos(5)+5*np.sin(x)))

# ~~~~~~~~~~~~~~
# Campos de fase
# ~~~~~~~~~~~~~~

v_line = np.linspace(-5, 5, 20)
y_line = np.linspace(-5, 5, 20)
v,y = np.meshgrid(v_line, y_line)

Y = v

V1 = -5*v - 4*y

V2 = -4*v - 4*y

V3= -4*v - 5*Y

# ~~~~~~~~~~~~~~~~~
# Plotando gráficos
# ~~~~~~~~~~~~~~~~~

fig, axes = plt.subplots(3, 2)

axes[0, 0].plot(x, solucao1(x), label='')
axes[0, 0].set_title("Gráfico 1")
axes[0, 0].grid(True)

axes[0, 1].quiver(v, y, V1,Y)
axes[0, 1].set_title("Plano de fase")
axes[0, 1].grid(True)

axes[1, 0].plot(x, solucao2(x), label='')
axes[1, 0].set_title("Gráfico 2")
axes[1, 0].grid(True)

axes[1, 1].quiver(v, y, V2, Y)
axes[1, 1].set_title("Plano de fase")
axes[1, 1].grid(True)

axes[2, 0].plot(x, solucao3(x), label='')
axes[2, 0].set_title("Gráfico 2")
axes[2, 0].grid(True)

axes[2, 1].quiver(v, y, V3, Y)
axes[2, 1].set_title("Plano de fase")
axes[2, 1].grid(True)

plt.grid(True) 
plt.show()