import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ln, = ax.plot([], [], 'ro')
plt.title('The Fall of the rock')
plt.xlabel('Axis X')
plt.ylabel('Axis Y')


def volume(t, resistance=int(input()), v_start=50, g=9.8, a=np.pi/4):
    x = v_start*np.cos(a)*t - resistance*t**2
    y = v_start*np.sin(a)*t - g*(t**2)/2 + resistance*t**2
    return x, y


def init():
    ax.set_xlim(0, 2000)
    ax.set_ylim(-4000, 4000)


def animate(frame):
    ln.set_data(volume(frame)[0], volume(frame)[1])


ani = FuncAnimation(fig, animate, interval=30, init_func=init, frames=np.linspace(0, 30, 100))
plt.show()



