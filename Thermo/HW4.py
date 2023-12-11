import matplotlib.pyplot as plt
import numpy as np

V_r = np.arange(0.5, 10, 0.001)
T_r = 9/4/V_r - 2/3/V_r**2 + 1/4/V_r**3

plt.scatter(V_r, T_r)
plt.xlabel('V_r')
plt.ylabel('T_r')

plt.savefig('HW4.png')
