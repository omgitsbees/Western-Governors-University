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

# Define variables for bivariate analysis
continuous_vars = ['age', 'bmi']
categorical_vars = ['sex', 'smoker']

# Bivariate analysis: Continuous vs Continuous
for var in continuous_vars:
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=data[var], y=data['charges'], alpha=0.7, color='blue')
    plt.title(f'Relationship between {var.capitalize()} and Charges')
    plt.xlabel(var.capitalize())
    plt.ylabel('Charges')
    plt.show()

# Bivariate analysis: Continuous vs Categorical
for var in categorical_vars:
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=data[var], y=data['charges'], palette='viridis')
    plt.title(f'Relationship between {var.capitalize()} and Charges')
    plt.xlabel(var.capitalize())
    plt.ylabel('Charges')
    plt.show()
