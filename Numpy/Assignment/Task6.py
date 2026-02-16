import numpy as np
# Same marks array (example)
marks = np.array([45, 67, 89, 34, 56, 78, 90, 62, 50, 72])

# 1. Sort the array
sorted_marks = np.sort(marks)

# 2. Percentiles
p25 = np.percentile(marks, 25)
p50 = np.percentile(marks, 50)
p75 = np.percentile(marks, 75)

# 3. Count students scoring above average
average = np.mean(marks)
above_avg_count = np.sum(marks > average)

# Printing results
print("Original Marks:", marks)
print("Sorted Marks:", sorted_marks)
print("25th Percentile:", p25)
print("50th Percentile (Median):", p50)
print("75th Percentile:", p75)
print("Average Marks:", average)
print("Number of students scoring above average:", above_avg_count)
