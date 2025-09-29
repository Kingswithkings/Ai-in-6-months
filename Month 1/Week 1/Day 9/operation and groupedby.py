# Add a derived column
import numpy as np
import pandas as pd

df = pd.read_csv('people.csv')

df['passed'] = np.where(df['score'].astype(int) >= 80, True, False)
print(df)

# Groupby example (by passed)
print('\nGroup counts:\n', df.groupby('passed').size())