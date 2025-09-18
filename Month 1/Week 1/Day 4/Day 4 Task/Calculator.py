# Mini Calculator that can add, subtract, multiply and divide
# 🛠 Hands-On Practice
# Create a Python file `calculator.py` with functions: `add`, `subtract`, `multiply`, `divide`.  
# Import it into a separate script (`main.py`) and use it.  
# Write a lambda function that sorts a list of tuples by the second element.
 
 
def add (x, y):
    return x + y

def subtract (x, y):
    return x - y

def multiply (x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y