import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Load the dataset
file_path = '/Users/kylecolby/Documents/D599/Task 2/Health Insurance Dataset.xlsx'  # Replace with your file path
data = pd.read_excel(file_path)

# Convert 'charges' to numeric
data['charges'] = pd.to_numeric(data['charges'], errors='coerce')

# Create BMI categories
bins = [0, 18.5, 24.9, 29.9, 100]
labels = ['Underweight', 'Normal weight', 'Overweight', 'Obese']
data['bmi_category'] = pd.cut(data['bmi'], bins=bins, labels=labels)

# Drop rows with missing data
data_cleaned = data.dropna(subset=['charges', 'bmi_category', 'smoker'])

# Perform two-way ANOVA
model = ols('charges ~ C(smoker) * C(bmi_category)', data=data_cleaned).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Print the results
print("Two-Way ANOVA Results:")
print(anova_table)
