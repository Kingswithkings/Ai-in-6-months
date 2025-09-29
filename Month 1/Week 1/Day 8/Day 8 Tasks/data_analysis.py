import pandas as pd
import matplotlib.pyplot as plt

def load_and_plot_ages(filepath='people.csv'):
    """
    Loads data from a CSV file, prints basic stats, and plots the ages.
    Requires pandas and matplotlib to be installed:
    pip install pandas matplotlib
    """

    try:
        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv(filepath)
        print(f"Sucessfully loaded data from {filepath}")
        print("\nFirst 5 rows of data:")
        print(df.head())

        # Basic Statistics
        print("\nAge statistics:")
        print(df['age'].describe())

        # Plotting the ages using matplotlib
        plt.figure(figsize=(10, 6))
        # Create a bar plot where x-axis is the name and y-axis
        plt.bar(df['name'], df['age'], color='skyblue')

        plt.title('Ages of People')
        plt.xlabel('Person Name')
        plt.ylabel('Age (Years)')
        plt.grid(axis='y', linestyle='--')
        plt.tight_layout() # Adjust layout to prevent labels from being cut off
        plt.show()

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found. Ensure 'people.csv")
    except ImportError:
        print("Error: pandas or matplotlib is not installed. Please run 'pip install pandas matplotlib'")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

if __name__ == "__main__":
    load_and_plot_ages()
