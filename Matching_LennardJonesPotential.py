import matplotlib.pyplot as plt
import numpy as np

L = 1
hc = 1

psi = 1
x = 1
dx = 0.1
dpsi = 1 / np.sqrt(0.0508895)
E = 20
dE = 0.02
x_list = []
psi_list = []


def LJP(x):
    return 4 * 50 * ((x**(-12)) - (x**(-6)))


while True:
    x = 0
    dpsi = 1 / np.sqrt(0.0508895)
    psi = 0

    while x <= L:
       # rate(10000)
        ddpsi = -2 * hc * E * psi
        dpsi = dpsi + ddpsi * dx
        psi = psi + dpsi * dx

        x = x + dx
        x_list.append(x)
        psi_list.append(psi)

    if abs(psi) < 0.001:

        print(E)
        print(psi)
        break
    E = E + dE


plt.scatter(x_list, psi_list)
plt.grid()
# plt.plot(x_list, psi_list)
plt.show()
