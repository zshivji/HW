import numpy as np
import matplotlib.pyplot as plt

R = 8.314 # J/mol-K
delta_h_25 = 2442.3*18 # J/mol
P_vap_25 = 3.169 # kPa
T_C = np.arange(15, 35+1, 0.5) # C
T_K = T_C + 273.15 # K

P = P_vap_25 * np.exp(delta_h_25 * (1/298.15 - 1/T_K)/R) 

T_table = np.array([15, 20, 25, 30, 35]) # K
P_table = np.array([1.7051, 2.339, 3.169, 4.246, 5.628]) # kPa

plt.plot(T_C, P)
plt.plot(T_table, P_table)

plt.xlabel('Temperature (K)')
plt.ylabel('Vapor Pressure (kPa)')
plt.legend(['Clausius-Clapeyron', 'Steam Table'])

plt.savefig('HW6.png')
