import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- Data Setup ---
# Load people.csv. 
# NOTE: The 'score' column is not in the original people.csv, 
# so we create a mock 'score' column (as done in the previous step) 
# for the histogram to work without error.
try:
    df = pd.read_csv('people.csv')
except FileNotFoundError:
    print("Error: 'people.csv' not found. Please ensure it is in the current directory.")
    exit()

# Add mock 'score' column for demonstration
np.random.seed(42) # for reproducible random scores
# Assuming 10 rows in people.csv based on earlier context
if 'score' not in df.columns or df['score'].isnull().all():
    df['score'] = np.random.randint(50, 101, size=len(df))

# --- Plotting the Histogram ---
plt.figure(figsize=(8, 5))

# Use the correct function name: plt.savefig()
# Convert 'score' to integer type for cleaner histogram bins
plt.hist(df['score'].astype(int), bins=8, edgecolor='black', alpha=0.7, color='teal') 

plt.title('Score Distribution')
plt.xlabel('Score')
plt.ylabel('Count')
plt.grid(axis='y', alpha=0.5)

# Fix the typo: 'savefigfig' -> 'savefig'
plt.savefig('score_histogram.png')

plt.show()

print("\nHistogram generated successfully:")
print("- Displayed on screen.")
print("- Saved to 'score_histogram.png'.")

