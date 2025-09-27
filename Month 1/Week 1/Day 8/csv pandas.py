import pandas as pd

df = pd.read_csv('people.csv')
print(df)

# Basic operations
print('\nAverage age:', df['age'].astype(int).mean())
print('Average score:', df['score'].astype(int).mean())

# Save filtered CSV
high_scores = df[df['score'].astype(int) > 85]
high_scores.to_csv('high_scores.csv', index=False)
print('\nWrote high_scores.csv')