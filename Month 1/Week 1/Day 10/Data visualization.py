import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load or create sample data
try:
    df = pd.read_csv('people.csv')
except FileNotFoundError:
    df = pd.DataFrame({'name':['Alice', 'Bob', 'Dave', 'Eve', 'Kings'],
                       'score':[88,95,79,82,90,76],
                       'group':['A','B','A','B','A','B']})
    df.to_csv('people.csv', index=False)

print('DataFrame loaded:')
print(df)