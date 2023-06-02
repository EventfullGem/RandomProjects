import numpy as np

# Dtype = data type (default is float64)
x = np.arange(0, 5, 1, dtype=np.int64)

print(x)

a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [1, 2, 3, 4, 5]])
# Prints the first "section" of the array# 
print(a[0])
# Creates an "empty" array (all values are close enough to 0)
print(np.empty(12))
# First number, last number, step size
print(np.arange(0, 10, .2))
# Array with values spaced equaly between the first and last number (21 numbers at equal intervals from 0 to 10)
print(np.linspace(0, 10, num=21))

