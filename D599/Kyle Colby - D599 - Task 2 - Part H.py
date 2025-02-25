import pandas as pd
from scipy.stats import kruskal

# Load the dataset
file_path = '/Users/kylecolby/Documents/D599/Task 2/Health Insurance Dataset.xlsx'  # Replace with your file path
data = pd.read_excel(file_path)

# Convert 'charges' to numeric, handling any potential errors
data['charges'] = pd.to_numeric(data['charges'], errors='coerce')

# Drop rows with missing data relevant to the analysis
data_cleaned = data.dropna(subset=['charges', 'children'])

# Group charges by the number of children
groups = [data_cleaned[data_cleaned['children'] == n]['charges'] for n in data_cleaned['children'].unique()]

# Perform the Kruskal-Wallis H test
stat, p = kruskal(*groups)

# Print the results
print("Kruskal-Wallis H Test Results:")
print(f"Statistic: {stat}")
print(f"P-value: {p}")

# Interpretation
alpha = 0.05
if p < alpha:
    print("Reject the null hypothesis: There is a significant difference in median charges between groups.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in median charges between groups.")
