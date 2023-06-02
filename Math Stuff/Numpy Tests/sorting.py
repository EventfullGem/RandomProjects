import numpy as np

# Create our unsorted array
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])

print(arr)
# Python's built-in sort function
arr.sort()

# sorts and prints the array (NPs sort function)
print(np.sort(arr))

''' 
argsort: an indirect sort along a specified axis,

lexsort: an indirect stable sort on multiple keys,

searchsorted: will find elements in a sorted array, and

partition: a partial sort. 
'''
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])

print(np.concatenate((x, y), axis=0))

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(np.concatenate((a, b), axis=0))
goofyArray = np.concatenate((a, b), axis=0)
# Prints the size of the array
print(goofyArray.size)

# Reshapes the array into a 4x2 array
print(goofyArray.reshape(4, 2))

# Or, you can do this:
print(np.reshape(goofyArray, newshape=(4, 2)))

# Currently on https://numpy.org/devdocs/user/absolute_beginners.html#how-to-convert-a-1d-array-into-a-2d-array-how-to-add-a-new-axis-to-an-array