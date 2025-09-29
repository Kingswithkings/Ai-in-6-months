import math

# --- Calculator Functions ---

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the division result of two numbers, raising an error on zero division."""
    if b == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    return a / b

def power(a, b):
    """
    New function: Returns the result of raising 'a' to the power of 'b'.
    Example: power(2, 3) = 8
    """
    return a ** b

def modulus(a, b):
    """Returns the remainder of the division of a by b."""
    if b == 0:
        raise ZeroDivisionError('Cannot modulo by zero')
    return a % b

# Dictionary of available operations
ops = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide,
    'power': power,
    'mod': modulus,
}

# --- Tests ---

def run_tests():
    """Performs assertion tests on all calculator functions."""
    print("Running assertion tests...")

    # Test 'add'
    assert add(2, 3) == 5, "Add test failed"
    assert add(-1, 5) == 4, "Add test failed (negative)"

    # Test 'subtract'
    assert subtract(5, 2) == 3, "Subtract test failed"
    assert subtract(10, 20) == -10, "Subtract test failed (negative result)"

    # Test 'multiply'
    assert multiply(3, 4) == 12, "Multiply test failed"
    assert multiply(5, 0) == 0, "Multiply test failed (by zero)"

    # Test 'divide'
    assert divide(10, 2) == 5.0, "Divide test failed"
    assert divide(10, 4) == 2.5, "Divide test failed (float result)"
    
    # Test 'power' (Extension)
    assert power(2, 3) == 8, "Power test failed (2^3)"
    assert power(5, 0) == 1, "Power test failed (x^0)"
    assert power(4, 0.5) == 2.0, "Power test failed (sqrt)"

    # Test 'modulus'
    assert modulus(10, 3) == 1, "Modulus test failed"
    assert modulus(9, 3) == 0, "Modulus test failed (exact division)"

    # Test ZeroDivisionError for 'divide'
    try:
        divide(1, 0)
        raise AssertionError('Expected ZeroDivisionError for divide')
    except ZeroDivisionError:
        pass # Test passed

    # Test ZeroDivisionError for 'modulus'
    try:
        modulus(1, 0)
        raise AssertionError('Expected ZeroDivisionError for modulus')
    except ZeroDivisionError:
        pass # Test passed

    print("All calculator tests passed successfully!")

if __name__ == "__main__":
    run_tests()
    print("\nAvailable operations:", ', '.join(ops.keys()))
    
    # Demonstrate the new 'power' function
    base = 3
    exp = 4
    result = ops['power'](base, exp)
    print(f"{base} to the power of {exp} = {result}")
