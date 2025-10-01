import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load or create sample data
try:
    df = pd.read_csv('people.csv')
except FileNotFoundError:
    df = pd.DataFrame({'name':['Alice','Bob','Carol','Dave','Eve','Frank'],
                       'age':[23,30,27,45,34,28],
                       'score':[88,95,79,82,90,76],
                       'group':['A','B','A','B','A','B']})
    df.to_csv('people.csv', index=False)

print('DataFrame loaded:')
print(df)


# Group by 'group' and compute statistics
grouped = df.groupby('group').agg({'score': ['mean', 'median', 'count']})
print(grouped)

# Flaten MultiIndex columns
grouped.columns = ['_'.join(col).strip() for col in grouped.columns.values]
print('\nFlattened grouped:\n', grouped)

# Bar plot of mean score per group
plt.figure()
grouped['score_mean'].plot(kind='bar')
plt.title('Mean Score bt Group')
plt.xlabel('Group')
plt.ylabel('Mean Score')
plt.savefig('mean_score_by_group.png')
plt.show()