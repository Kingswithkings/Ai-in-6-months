import math_utils

# Example operations
print("--- Calculator operations ---")
print(f"10 + 5 = {math_utils.add(10, 5)}")
print(f"10 / 2 = {math_utils.divide(10, 2)}")
print(f"sqrt(9) = {math_utils.square_root(9)}")
print(f"sqrt(25) = {math_utils.square_root(25)}")

# Get and print the operation history
print("\n--- Operation history ---")
print(math_utils.get_history())