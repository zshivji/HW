# Kinetics HW1
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Problem 4a

# define diff eq
def X(y, t):
    A, B, C = y
    dAdt = - k1*A*B + k2*C
    dBdt = - k1*A*B + k2*C
    dCdt = k1*A*B - k2*C
    dXdt = [dAdt, dBdt, dCdt]
    return dXdt

# define input parameters
k1 = 6
k2 = 3
A0 = 1
B0 = 2
C0 = 0

X0 = [A0, B0, C0]

# define timescalee
t0 = 0
tf = 5
t = np.linspace(t0, tf, 101)

# solve
y = odeint(X, X0, t)

# plot
plt.plot(t, y[:, 0])
plt.plot(t, y[:, 1])
plt.plot(t, y[:, 2])
plt.xlabel('Time (hr)')
plt.ylabel('Concentration (mols)')
plt.legend(['[A]', '[B]', '[C]'])
plt.show()
plt.savefig('Kinetics_HW1_4a')

print(y[-1, 0])