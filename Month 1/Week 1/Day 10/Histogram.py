import pandas as pd              # CORRECT: Pandas for read_csv and DataFrame operations
import numpy as np               # CORRECT: NumPy for array/numerical operations
import matplotlib.pyplot as plt  # CORRECT: matplotlib.pyplot for plotting functions

# Load the data using Pandas
df = pd.read_csv('people.csv')

# --- 1. Histogram of scores ---
plt.figure(figsize=(7, 5))
plt.hist(df['score'].astype(int), bins=8, edgecolor='black', color='#4CAF50')
plt.title('Score Distribution', fontsize=16, fontweight='bold')
plt.xlabel('Score Range', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.grid(axis='y', alpha=0.6, linestyle='--')
plt.savefig('score_histogram.png')
plt.show()

# --- 2. Boxplot ---
plt.figure(figsize=(5, 7))
plt.boxplot(df['score'].astype(int), vert=True, patch_artist=True, 
            boxprops=dict(facecolor='#2196F3', color='black'),
            medianprops=dict(color='red'))
plt.title('Score Boxplot', fontsize=16, fontweight='bold')
plt.ylabel('Score', fontsize=12)
plt.xticks([1], ['All Scores'])
plt.savefig('score_boxplot.png')
plt.show()
