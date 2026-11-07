import numpy as np
import matplotlib.pyplot as plt

g= 9.8
v0= float(input('Enter the initial velocity: '))
angle= float(input("Enter the angle the object is thrown in: "))
theta = np.deg2rad(angle)

T= (2*v0*np.sin(theta))/g

t=np.linspace(0, T, 300)

def x(t):
    return v0*np.cos(theta)*t
def y(t):
    return v0*np.sin(theta)*t-0.5*g*(t**2)

plt.plot(x(t), y(t))
plt.xlabel("horizontal")
plt.ylabel("vertical")
plt.legend()
plt.show()