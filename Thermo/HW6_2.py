import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy.optimize import fmin

Tr = np.linspace(.2, 1, 100)

# get spinodal curves
V_spin = np.array([np.roots((-4*T, 9, -6, 1))[1::-1] for T  in Tr])

P_spin_1 = 8*Tr/(3*V_spin[:, 0]-1) - 3/(V_spin[:, 0]**2)
P_spin_2 = 8*Tr/(3*V_spin[:, 1]-1) - 3/(V_spin[:, 1]**2)

# get coexistence curves (maxwell construction)

def maxwell(Pr, Tr): # slide 35 lecture 11/12
    V = np.roots([-3*Pr, Pr+8*Tr, -9, 3])
    integral = 8/3*Tr*np.log((3*max(V)-1)/(3*min(V)-1)) +\
    3/max(V)-3/min(V) -\
    (8*Tr/(3*max(V)-1) - 3/max(V)**2)*max(V)+\
    (8*Tr/(3*min(V)-1) - 3/min(V)**2)*min(V)
    return abs(integral)
     
Pr_coex = []
Vr_coex = []
for i, T in enumerate(Tr):
    Pr_coex.append(fmin(lambda x: maxwell(x, T), 0.5, disp=False)[0]) # get P_coex when equal areas satisified
    Vr = abs(np.roots((-3*Pr_coex[-1], Pr_coex[-1]+8*T, -9, 3)))
    Vr_coex.append([min(Vr), max(Vr)])

fig, ax = plt.subplots(1, 2, figsize = (16, 8))

ax[0].plot(Tr, P_spin_1, c = 'orange', label = '_nolegend_')
ax[0].plot(Tr, P_spin_2, c = 'orange', label = 'Spinodal')
ax[0].plot(Tr, Pr_coex, c='teal', label = 'Coexistance')
ax[0].set_ylim(0, 1)
ax[0].set_xlabel('Pr', fontsize = 16)
ax[0].set_ylabel('Tr', fontsize = 16)
ax[0].legend()

ax[1].plot(V_spin[:, 0], Tr, c = 'orange',label = 'Spinodal')
ax[1].plot(V_spin[:, 1], Tr, c = 'orange', label = '_nolegend_')
ax[1].plot(Vr_coex, Tr, c = 'teal', label = ['Coexistance', '_nolegend_'])
ax[1].set_xlim(0, 5)
ax[1].set_xlabel('Tr', fontsize = 16)
ax[1].set_ylabel('Vr', fontsize = 16)
ax[1].legend()


plt.savefig('HW6_2_Tr_Vr.png')