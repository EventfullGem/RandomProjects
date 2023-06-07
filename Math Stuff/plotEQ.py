# Don't know what this does but it works

# importing the required modules
import matplotlib.pyplot as plt
import numpy as np
# import varstorage as vs

# setting the x - coordinates (starting value, end value, step size)
# 2*(np.pi) is 2pi
# Can also use a normal array
# Ex: x = vs.x
x = np.arange(0, 40, 0.01)
# setting the corresponding y - coordinates
y = np.sin(x) 
# ex:  np.log(np.square(x))

# plotting the points
plt.plot(x, y)

# function to show the plot
plt.show()
