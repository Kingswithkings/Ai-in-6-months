import Calculator

# Use the imported functions
result_add = Calculator.add(10, 5)
result_subtract = Calculator.subtract(10, 5)
result_multiply = Calculator.multiply(10, 5)
result_divide = Calculator.divide(10, 5)

print(f"Addition: 10 + 5 = {result_add}")
print(f"Subtraction: 10 - 5 = {result_subtract}")
print(f"Multiplication: 10 * 5 = {result_multiply}")
print(f"Division: 10 / 5 = {result_divide}")

# Example of a zero division
result_zero_divide = Calculator.divide(10, 0)
print(f"Division by zero: {result_zero_divide}")