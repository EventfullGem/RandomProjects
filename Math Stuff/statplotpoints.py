# Testing graphing on this now
# very basic plot, can use this to expand later
import matplotlib.pyplot as plt
import varstorage as vs
# Imports required module


# Sets the Values
x1 = vs.x
y1 = vs.y

# Plots the points and colors them with a dashed style. I don't know why the formatting is this way
# it might work if you change it, but it might not
plt.plot(x1, y1, color='gray', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='blue', markersize=6, label="Line 1")

# Naming the X axis
plt.xlabel('X Axis')

# Naming the Y axis
plt.ylabel('Y Axis')

# Title of the graph
plt.title('Graph with points')
# Color coded legend
plt.legend()
# Shows the graph
plt.show()
