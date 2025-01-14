import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/Users/kylecolby/Documents/D599/Task 2/Health Insurance Dataset.xlsx'  # Replace with the correct path
data = pd.read_excel(file_path)

# Display initial dataset structure
print("Dataset loaded successfully.")
print(data.info())

# Convert 'charges' to numeric, handling any potential errors
data['charges'] = pd.to_numeric(data['charges'], errors='coerce')

# Define variables for univariate analysis
continuous_vars = ['age', 'bmi']
categorical_vars = ['sex', 'smoker']

# Plot distributions for continuous variables
for var in continuous_vars:
    plt.figure(figsize=(8, 5))
    sns.histplot(data[var], kde=True, bins=30, color='blue')
    plt.title(f"Distribution of {var.capitalize()}")
    plt.xlabel(var.capitalize())
    plt.ylabel('Frequency')
    plt.show()

# Plot distributions for categorical variables
for var in categorical_vars:
    plt.figure(figsize=(8, 5))
    sns.countplot(x=data[var], palette='viridis', order=data[var].value_counts().index)
    plt.title(f"Distribution of {var.capitalize()}")
    plt.xlabel(var.capitalize())
    plt.ylabel('Count')
    plt.show()
