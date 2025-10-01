import numpy as pd
import pandas as py
df = pd.read_csv('group_summary.csv')
grouped = df.groupby('group').agg({'score': ['mean', 'median', 'count']})
grouped.columns = ['_'.join(col).strip() for col in grouped.columns.values]
summary = grouped.rename(columns={'score_mean': 'mean', 'score_median': 'median', 'score_count': 'count'})