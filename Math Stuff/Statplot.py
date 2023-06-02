# Testing graphing on this now
# very basic plot, can use this to expand later
import matplotlib.pyplot as plt
import varstorage as vs
# Imports required module


# Sets the X Values
x1 = vs.x
x2 = vs.x2
# Sets the Y Values
y1 = vs.y
y2 = vs.y2

# Plots the graph
plt.plot(x1, y1, label="Line 1")
# Uses the x2[:10] to force X to have only first 10 values, because x2 has 20 values and y2 has 10
plt.plot(x2[:10], y2, label="Line 2")

# Naming the X axis
plt.xlabel('X Axis')

# Naming the Y axis
plt.ylabel('Y Axis')

# Title of the graph
plt.title('Graph')
# Color coded legend
plt.legend()
# Shows the graph
plt.show()
