import logging
import os
import math

# Configure logger
LOG_FILE = 'calculator.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# --- Calculator Functions (Updated to include logging) ---

def add(a, b):
    result = a + b
    logging.info(f"add {a} {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    logging.info(f"subtract {a} {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    logging.info(f"multiply {a} {b} = {result}")
    return result

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    result = a / b
    logging.info(f"divide {a} {b} = {result}")
    return result

def power(a, b):
    result = a ** b
    logging.info(f"power {a} {b} = {result}")
    return result

def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError('Cannot modulo by zero')
    result = a % b
    logging.info(f"mod {a} {b} = {result}")
    return result

# --- Extension 1: Unary Operation (sqrt) ---

def square_root(a):
    if a < 0:
        raise ValueError('Cannot take the square root of a negative number')
    result = math.sqrt(a)
    logging.info(f"sqrt {a} = {result}")
    return result

# --- Extension 2: History Function ---

def show_history():
    """Reads and prints the content of the log file."""
    if not os.path.exists(LOG_FILE):
        print("No history found yet.")
        return
    print("\n--- Calculation History ---")
    with open(LOG_FILE, 'r') as f:
        print(f.read())
    print("-----------------------------\n")

# --- Operation Dictionaries ---
binary_ops = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide,
    'power': power,
    'mod': modulus,
}

unary_ops = {
    'sqrt': square_root,
}

# --- Interactive Loop (Extended) ---
print('Calculator functions and logger initialized')
print('Simple Calculator — type commands like: add 4 5 or sqrt 9')
print('Available binary ops:', ', '.join(binary_ops.keys()))
print('Available unary ops:', ', '.join(unary_ops.keys()))
print("Type 'history' to view logs or 'exit' to quit")

while True:
    try:
        line = input('> ').strip()
        if not line:
            continue
        if line.lower() == 'exit':
            print('Goodbye!')
            break
            
        # Extension 2: History Command
        if line.lower() == 'history':
            show_history()
            continue

        parts = line.split()
        op = parts[0]
        
        # Check for Unary Operation (e.g., sqrt 9)
        if op in unary_ops:
            if len(parts) != 2:
                print('Usage: <op> <num1>')
                continue
            try:
                a = float(parts[1])
            except ValueError:
                print('Please enter a valid number')
                continue
            try:
                result = unary_ops[op](a)
            except ValueError as e:
                print('Error:', e)
                continue
            print('Result =', result)
        
        # Check for Binary Operation (e.g., add 4 5)
        elif op in binary_ops:
            if len(parts) != 3:
                print('Usage: <op> <num1> <num2>')
                continue
            a_str, b_str = parts[1], parts[2]
            try:
                a = float(a_str)
                b = float(b_str)
            except ValueError:
                print('Please enter valid numbers')
                continue
            try:
                result = binary_ops[op](a, b)
            except ZeroDivisionError as e:
                print('Error:', e)
                continue
            print('Result =', result)
        
        else:
            print('Unknown operation. Available:', 
                  ', '.join(binary_ops.keys()) + ', ' + ', '.join(unary_ops.keys()))
            
    except KeyboardInterrupt:
        print('\nInterrupted. Exiting.')
        break