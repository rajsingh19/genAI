import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

result = np.split(arr, 3)
print(result)


arr = np.array([1, 2, 3, 4, 5])

result = np.array_split(arr, 3)
print(result)
