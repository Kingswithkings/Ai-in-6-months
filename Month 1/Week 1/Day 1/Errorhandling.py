# Division with eror handling (Edit / run this cell)
try:
    a = float(input('Enter numerator: '))
    b = float(input('Enter denominator: '))
    print('Result =', a / b)
except ZeroDivisionError:
    print('Error: Cannot divide by zero')
except ValueError:
    print('Error: please enter valid numbers')