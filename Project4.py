# Lauren Roe
# CST-305
# This is my own work

# This program plots the equations found as the solutions to a system of differential equations
# The equations model the loss or corruption of data


import numpy as np                  # imported to define p as a space of numbers
import matplotlib.pyplot as plt     # imported to see the solution as a plot


def x1(t):                      # this function returns the x1 equation
    x1 = np.exp(-t/20)          # the equation calculated
    return x1                   # returns x1


def x2(t):                      # this function returns the x2 equation
    x2 = -np.exp(-t/20)         # the equation calculated
    return x2                   # returns x2


t = np.linspace(0, 10, 100)     # range of values for t

plt.plot(t, x1(t), 'g--', linewidth=2, label='x1')      # points for x1
plt.xlabel('x')                         # labels x-axis with x
plt.ylabel('y')                         # labels y-axis with y
plt.legend()                            # plots the key with the label of the equation
plt.show()                              # displays the plot

plt.plot(t, x2(t), 'b:', linewidth=2, label='x2')       # points for x2
plt.xlabel('x')                         # labels the x-axis with x
plt.ylabel('y')                         # labels the y-axis with y
plt.legend()                            # plots the key with the label of the equation
plt.show()                              # displays the plot

plt.plot(t, x1(t), 'g--', linewidth=2, label='odeint')  # points for x1
plt.plot(t, x2(t), 'b:', linewidth=2, label='odeint')   # points for x2
plt.xlabel('x')                         # labels the x-axis with x
plt.ylabel('y')                         # labels the y-axis with y
plt.legend()                            # plots the key with the equation labels
plt.show()                              # displays the plot with both x1 and x2
