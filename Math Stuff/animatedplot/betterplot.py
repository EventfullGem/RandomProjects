# User input plot

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# initial data
data = [3, 6, 2, 1, 9]
# create the figure and axes objects
fig, ax = plt.subplots()

# Animate function 
def animate(i):
    with open('data.txt', 'r') as f:
        for line in f:
            data.append(int(line.strip()))
    ax.clear()
    ax.plot(data[-5:]) # Plot last 5 data points

# call function
ani = FuncAnimation(fig, animate, interval=1000)

plt.show()
