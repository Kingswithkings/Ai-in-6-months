import pandas as pd

# Read CSV (people.csv created earlier in Day 8)
try:
    df = pd.read_csv('people.csv')
except FileNotFoundError:
    # create sample if missing
    df = pd.DataFrame({'name':['Alice', 'Kings', 'Carol'], 'age':[23,34,27], 'score':[88,95,79]})
    df.to_csv('people.csv', index=False)
    df = pd.read_csv('people.csv')

print('DataFrame:')
print(df)