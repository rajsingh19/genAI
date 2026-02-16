# Fancy indexing allows you to access multiple array elements at once using arrays of indices. This can be useful for selecting specific elements or rearranging the order of elements in an array.
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[[0, 2, 4]])
