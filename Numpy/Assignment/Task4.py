import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
rsum = np.sum(data , axis = 1)
print("Sum of each row:", rsum)

csum = np.sum(data , axis = 0)
print("Sum of each column:", csum)

min = np.min(data)
print("Minimum value in the array:", min)

max = np.max(data)
print("Maximum value in the array:", max)

mean = np.mean(data)
print("Mean value of the array:", mean)