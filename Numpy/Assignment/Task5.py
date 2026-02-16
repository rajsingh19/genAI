import numpy as np
arr = np.array([78,85,90,66,72,88,95,60])
print(arr.mean())
print(np.median(arr))
print(arr.var())
print(arr.std())
print(arr.min())
print(arr.max())

range_value = np.max(arr) - np.min(arr)

print(range_value)