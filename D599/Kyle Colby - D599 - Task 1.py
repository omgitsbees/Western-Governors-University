import pandas as pd

# Load the dataset
file_path = '/Users/kylecolby/Documents/D599/Task 1/Employee Turnover Dataset.csv'
data = pd.read_csv(file_path)

# Strip extra spaces from column names to avoid errors
data.columns = data.columns.str.strip()

# Step 1: Remove duplicate entries
data = data.drop_duplicates()

# Step 2: Handle missing values
# Fill missing values in 'NumCompaniesPreviouslyWorked' with the median
data['NumCompaniesPreviouslyWorked'] = data['NumCompaniesPreviouslyWorked'].fillna(data['NumCompaniesPreviouslyWorked'].median())

# Fill missing values in 'AnnualProfessionalDevHrs' with the mean
data['AnnualProfessionalDevHrs'] = data['AnnualProfessionalDevHrs'].fillna(data['AnnualProfessionalDevHrs'].mean())

# Fill missing values in 'TextMessageOptIn' with the mode
data['TextMessageOptIn'] = data['TextMessageOptIn'].fillna(data['TextMessageOptIn'].mode()[0])

# Step 3: Normalize inconsistent categorical entries
# Standardize 'PaycheckMethod' entries
data['PaycheckMethod'] = data['PaycheckMethod'].replace({
    'Mail Check': 'Mailed Check',
    'Mail_Check': 'Mailed Check',
    'Direct_Deposit': 'Direct Deposit',
    'DirectDeposit': 'Direct Deposit'
})

# Standardize 'JobRoleArea' entries
data['JobRoleArea'] = data['JobRoleArea'].replace({
    'Information_Technology': 'Information Technology',
    'InformationTechnology': 'Information Technology',
    'Human_Resources': 'Human Resources',
    'HumanResources': 'Human Resources'
})

# Step 4: Correct formatting errors
# Remove '$' from 'HourlyRate' and convert to numeric
data['HourlyRate'] = data['HourlyRate'].replace('[\$]', '', regex=True).astype(float)

# Step 5: Investigate and handle outliers
# Remove negative values from 'AnnualSalary' and 'DrivingCommuterDistance'
data = data[data['AnnualSalary'] >= 0]
data = data[data['DrivingCommuterDistance'] >= 0]

# Step 6: Save the cleaned dataset
output_path = '/Users/kylecolby/Documents/D599/Task 1/Employee_Turnover_Cleaned.csv'
data.to_csv(output_path, index=False)

# Display final cleaning report
print("Data cleaning complete. Cleaned dataset saved to", output_path)
