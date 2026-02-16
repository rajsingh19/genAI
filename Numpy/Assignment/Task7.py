import numpy as np

# Given data
sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])

# 1. Total weekly sales
total_sales = np.sum(sales)

# 2. Average daily sales
average_sales = np.mean(sales)

# 3. Highest and lowest sales
highest_sales = np.max(sales)
lowest_sales = np.min(sales)

# 4. Standard deviation
std_sales = np.std(sales)

# 5. Days where sales were above average
above_avg_days = np.where(sales > average_sales)[0]  # index of days
count_above_avg = np.sum(sales > average_sales)      # count of days

# Print results
print("Total Weekly Sales:", total_sales)
print("Average Daily Sales:", average_sales)
print("Highest Sales:", highest_sales)
print("Lowest Sales:", lowest_sales)
print("Standard Deviation:", std_sales)
print("Days with Sales Above Average (index):", above_avg_days)
print("Number of Days Above Average:", count_above_avg)
