import matplotlib.pyplot as plt
import numpy as np
  
# frequencies
x = np.arange(0, 40, 0.1)
ages = np.sin(x)
  
# setting the ranges and no. of intervals
range = (0, 1)
bins = np.arange(0, 1, 0.1)
  
# plotting a histogram
plt.hist(ages, bins, range, color = 'green',    
        histtype = 'bar', rwidth = 0.8)
  
# x-axis label
plt.xlabel('age')
# frequency label
plt.ylabel('No. of people')
# plot title
plt.title('My histogram')
  
# function to show the plot
plt.show()