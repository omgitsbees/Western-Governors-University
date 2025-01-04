import pandas as pd

# Step 2: Import Libraries and Dataset
data_file = 'C:/Users/kyleh/Downloads/D598 Data Set.xlsx'
df = pd.read_excel(data_file)

# Step 3: Check for Duplicates
duplicates = df[df.duplicated()]
print("Duplicate Rows:")
print(duplicates)

# Step 4: Group by State and Calculate Statistics
grouped_stats = df.groupby('Business State').agg({
    'Total Long-term Debt': ['mean', 'median', 'min', 'max'],
    'Total Equity': ['mean', 'median', 'min', 'max'],
    'Total Liabilities': ['mean', 'median', 'min', 'max'],
    'Total Revenue': ['mean', 'median', 'min', 'max'],
    'Profit Margin': ['mean', 'median', 'min', 'max']
}).reset_index()

print("Grouped Statistics by State:")
print(grouped_stats)

# Step 5: Filter for Negative Debt-to-Equity Ratios
negative_debt_to_equity = df[df['Debt to Equity'] < 0]
print("Businesses with Negative Debt-to-Equity Ratios:")
print(negative_debt_to_equity)

# Step 6: Calculate Debt-to-Income Ratio
df['Debt-to-Income'] = df['Total Long-term Debt'] / df['Total Revenue']

# Step 7: Merge DataFrames
final_df = df

# Step 8: Save or Display Results
final_df.to_excel('Final_Analysis_Output.xlsx', index=False)
print("Analysis Completed. Results saved as 'Final_Analysis_Output.xlsx'.")
