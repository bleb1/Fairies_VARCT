import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model_2BP(state, t):
    mu = 3.24859E+05
    x = state[0]
    y = state[1]
    z = state[2]
    x_dot = state[3]
    y_dot = state[4]
    z_dot = state[5]
    x_ddot = -mu * x / (x ** 2 + y ** 2 + z ** 2) ** (3 / 2)
    y_ddot = -mu * y / (x ** 2 + y ** 2 + z ** 2) ** (3 / 2)
    z_ddot = -mu * z / (x ** 2 + y ** 2 + z ** 2) ** (3 / 2)
    dstate_dt = [x_dot, y_dot, z_dot, x_ddot, y_ddot, z_ddot]
    return dstate_dt

# Начальные положения
X_0 = -2500
Y_0 = -5500
Z_0 = 3400
VX_0 = 7.76
VY_0 = 0.0
VZ_0 = 4.82
state_0 = [X_0, Y_0, Z_0, VX_0, VY_0, VZ_0]

t = np.linspace(0, 18 * 3600, 200)

sol = odeint(model_2BP, state_0, t)
X_Sat = sol[:, 0]
Y_Sat = sol[:, 1]
Z_Sat = sol[:, 2]

N = 50
phi = np.linspace(0, 2 * np.pi, N)
theta = np.linspace(0, np.pi, N)
theta, phi = np.meshgrid(theta, phi)

Venus_r = 6051.8  # Радиус Венеры
Venus_x = Venus_r * np.cos(phi) * np.sin(theta)
Venus_y = Venus_r * np.sin(phi) * np.sin(theta)
Venus_z = Venus_r * np.cos(theta)

fig = plt.figure()
axes = plt.axes(projection='3d')
axes.plot_surface(Venus_x, Venus_y, Venus_z, color='orange', alpha=0.7)
axes.plot3D(X_Sat, Y_Sat, Z_Sat, 'blue')
axes.view_init(25, 145)
plt.title('Задача двух тел')
axes.set_xlabel('X km')
axes.set_ylabel('Y km')
axes.set_zlabel('Z km')
plt.show()
