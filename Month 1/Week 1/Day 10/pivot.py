import pandas as pd
import numpy as np

# define the module
df = pd.read_csv('people.csv')

# Pivot table: average score by group
pivot = pd.pivot_table(df, values='score', index='group', aggfunc=np.mean)
print('Pivot table:\n', pivot)

# Example merge: create a summary dataframe and merge back
summary = df.groupby('group').agg(total_members=('name', 'count'), avg_score=('score', 'mean')).reset_index()
print('\summary:\n', summary)

merged = pd.merge(df, summary, on='group')
print('\nMerged sample:\n', merged.head())


summary.to_csv('group_summary.csv', index=False) # <--- Error happens here
print('saved group_summary.csv')

# List ncreated image files
import os 
images = [f for f in os.listdir('.') if f.endswith('.png')]
print('saved images:', images)