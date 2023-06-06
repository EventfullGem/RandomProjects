import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D


left = [1, 2, 3, 4, 5]
height = [1, 12.8, 3.67, .12, .22]

tick_label = ['Linux Terminal', 'Windows CMD', 'IntelliJ IDEA', 'WSL', 'Linux Terminal']

# plots the bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['#7DADD8', '#9C7DD8', '#9C7DD8', '#9C7DD8', '#7DADA8' ])

# naming the x-axis
plt.xlabel('Test Environment')
# naming the y-axis
plt.ylabel('Time to complete (seconds)')
# plot title
plt.title('Multi Core Speed Tests')

# create custom legend
legend_elements = [Line2D([0], [0], color='#7DADD8', lw=4, label='Raspberry Pi 4B 8GB'),
                   Line2D([0], [0], color='#9C7DD8', lw=4, label='i7-10750H CPU @ 2.6GHz'),
                   Line2D([0], [0], color='#7DADA8', lw=4, label='Xeon E5-645 v5 CPU @ 2.4GHz')]

# add legend to plot
plt.legend(handles=legend_elements)

# function to show the plot
plt.show()
