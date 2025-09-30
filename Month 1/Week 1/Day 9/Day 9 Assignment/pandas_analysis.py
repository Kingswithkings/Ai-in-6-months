import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_people_data(filepath='people.csv'):
    """
    Loads people.csv, adds a score column, assigns age groups, 
    shows group counts, and plots age vs score.
    
    Requires pandas, numpy, and matplotlib:
    pip install pandas numpy matplotlib
    """
    try:
        # Load the CSV file
        df = pd.read_csv(filepath)
        print(f"--- Data Loaded from {filepath} ---")
        print(df)
        
        # --- Task 1: Mock Score Column (for plotting) ---
        # Since 'score' doesn't exist, generate random scores between 50 and 100 
        # for a realistic scatter plot demonstration.
        np.random.seed(42) # for reproducible scores
        df['score'] = np.random.randint(50, 101, size=len(df))
        
        # --- Task 2: Add 'age_group' Column ---
        # Define the condition and corresponding values
        # 'young' if age < 30, 'adult' if age >= 30
        df['age_group'] = np.where(df['age'] < 30, 'young', 'adult')
        
        print("\n--- DataFrame with 'score' and 'age_group' ---")
        print(df)
        
        # --- Task 3: Show Counts per Group ---
        age_counts = df['age_group'].value_counts()
        print("\n--- Counts per Age Group ---")
        print(age_counts)
        
        # --- Task 4: Plot Age vs Score ---
        plt.figure(figsize=(10, 6))
        # Plotting score against age, coloring points by age_group
        groups = df.groupby('age_group')
        
        for name, group in groups:
            plt.plot(group['age'], group['score'], marker='o', linestyle='', markersize=8, label=name)
        
        plt.title('Person Age vs. Mock Score')
        plt.xlabel('Age (Years)')
        plt.ylabel('Mock Score')
        plt.legend(title='Age Group')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found. Ensure 'people.csv' is in the same directory.")
    except ImportError as e:
        print(f"Error: Required library not found. {e}")
        print("Please install necessary libraries: 'pip install pandas numpy matplotlib'")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    analyze_people_data()
