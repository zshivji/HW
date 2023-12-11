# Kinetics HW1
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Problem 6

# define diff eq
def X(y, t):
    R, L = y
    dRdt = k1*G*R - k2*L*R
    dLdt = k2*L*R - k3*L
    dXdt = [dRdt, dLdt]
    return dXdt

# define input parameters
G = 1
k1 = 1
k2 = 1
k3 = 1
R0 = 20
L0 = 1

X0 = [R0, L0]

# define timescalee
t0 = 0
tf = 100
t = np.linspace(t0, tf, 101)

# solve
y = odeint(X, X0, t)

# plot
plt.plot(t, y[:, 0])
plt.plot(t, y[:, 1])
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend(['Rabits', 'Lynxes'])
plt.show()
plt.savefig('Kinetics_HW1_6b')