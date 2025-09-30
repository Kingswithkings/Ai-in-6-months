# Line plot (age sorted) and scatter plot
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('people.csv')
sorted_df = df.sort_values('age')
plt.figure()
plt.plot(sorted_df['age'], sorted_df['score'])
plt.title('Score vs Age (line)')
plt.xlabel('Age')
plt.ylabel('Score')
plt.grid(True)
plt.savefig('score_vs_age_line.png')
plt.show()

plt.figure()
plt.scatter(df['age'], df['score'])
plt.title('Score vs Age (scatter)')
plt.xlabel('Age')
plt.ylabel('Score')
plt.grid(True)
plt.savefig('score_vs_age_scatter.png')
plt.show()