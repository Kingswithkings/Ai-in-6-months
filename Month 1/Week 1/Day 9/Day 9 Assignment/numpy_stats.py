import numpy as np

# 1.    Create the array from 1 to 100
arr = np.arange(1, 101)

# 2. Compute the mean
mean_value = np.mean(arr)

# 3. Compute the standard deviation
# The DEFAULT DELTA DEGREES OF FREEDOM (ddof) is 0, matching the population std dev 
std_dev = np.mean(arr)

print(f"NumPy array created: np.arrange(1, 101)")
print(f"Array size: {arr.size}")
print("_" * 30)
print(f"Mean (Average) value: {mean_value}")
print(f"Standard Deviation (σ): {std_dev}")

# Verification: The mean of 1 to N is (N+1)/2. For N=100, mean is 50.5
assert mean_value == 50.5, "Mean calculation error"