# Kinetics HW3
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Problem 1

# define diff eq
def X(y, t):
    A, B = y
    dAdt = - k*A*B
    dBdt = k*A*B
    dXdt = [dAdt, dBdt]
    return dXdt

# define input parameters
k = 0.02
A0 = 1
B0 = .1

X0 = [A0, B0]

# define timescalee
t0 = 0
tf = 500
t = np.linspace(t0, tf, 101)

# solve
y = odeint(X, X0, t)

# plot
plt.plot(t, y[:, 0])
plt.plot(t, y[:, 1])
plt.xlabel('Time (min)')
plt.ylabel('Concentration (M)')
plt.legend(['[A]', '[B]'])
plt.show()
plt.savefig('Kinetics_HW3_1')

print(y[-1, 0])