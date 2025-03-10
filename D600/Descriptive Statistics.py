# Selecting the dependent and independent variables
variables = [
    'IsLuxury', 'SquareFootage', 'NumBathrooms', 'NumBedrooms', 'BackyardSpace',
    'RenovationQuality', 'LocalAmenities', 'TransportAccess', 'Garage',
    'DistanceToCityCenter', 'Fireplace', 'AgeOfHome'
]

# Subset the dataset to include only the relevant variables
selected_data = housing_data[variables]

# Generate descriptive statistics for the selected variables
descriptive_stats = selected_data.describe(include='all').transpose()

# Add mode and unique value counts for categorical variables (e.g., 'Garage', 'Fireplace')
descriptive_stats['Mode'] = selected_data.mode().iloc[0]
descriptive_stats['Unique Values'] = selected_data.nunique()

# Save the descriptive statistics for review and visualization
import ace_tools as tools; tools.display_dataframe_to_user(name="Descriptive Statistics for Dependent and Independent Variables", dataframe=descriptive_stats) 
