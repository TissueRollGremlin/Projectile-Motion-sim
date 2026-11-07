import numpy as np
import matplotlib.pyplot as plt
import math

def inp():
    length = float(input("Enter the length of the string in meters: "))
    angleofoscillation = float(input("Enter the angle the pendulum is oscillated in: "))
    theta = np.deg2rad(angleofoscillation)
    return length, theta 

def main(length, theta0):
    g=9.8
    interval = 2*(math.pi)* (math.sqrt (length / g))

    dt = 0.001
    steps = int(3*interval/dt)

    theta = np.zeros(steps)
    omega = np.zeros(steps)
    theta[0]= theta0

    for i in range (steps -1):
        alpha = -(g/length)*np.sin(theta[i])
        omega [i+1]== omega[i]+ alpha*dt
        theta [i+1]== theta [i]  + omega[i+1]*dt

        t= np.arrange(steps) * dt

    plt.plot(t, np.deg2rad(theta))
    plt.xlabel("T(seconds)")
    plt.ylabel("angle(theta)")
    plt.legend()
    plt.show()

    import numpy as np
import matplotlib.pyplot as plt
import math

def inp():
    length = float(input("Enter the length of the string in meters: "))
    angleofoscillation = float(input("Enter the angle the pendulum is oscillated in: "))
    theta = np.deg2rad(angleofoscillation)
    return length, theta 

def main(length, theta0):
    g=9.8
    interval = 2*(math.pi)* (math.sqrt (length / g))

    dt = 0.001
    steps = int(3*interval/dt)

    theta = np.zeros(steps)
    omega = np.zeros(steps)
    theta[0]= theta0

    for i in range (steps -1):
        alpha = -(g/length)*np.sin(theta[i])
        omega [i+1] = omega[i]+ alpha*dt
        theta [i+1] = theta [i]  + omega[i+1] *dt

    t= np.arange(steps) * dt

    plt.plot(t, np.deg2rad(theta))
    plt.xlabel("T(seconds)")
    plt.ylabel("angle(theta)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":                         
    length, theta0 = inp()
    main(length, theta0)

