from sklearn.preprocessing import StandardScaler

# Select only the continuous predictor variables
continuous_vars = [
    "SquareFootage", "NumBathrooms", "NumBedrooms", "BackyardSpace", "CrimeRate",
    "SchoolRating", "AgeOfHome", "DistanceToCityCenter", "EmploymentRate", "PropertyTaxRate",
    "RenovationQuality", "LocalAmenities", "TransportAccess", "Floors", "Windows", "PreviousSalePrice"
]

# Standardize the selected variables
scaler = StandardScaler()
housing_df_standardized = housing_df.copy()
housing_df_standardized[continuous_vars] = scaler.fit_transform(housing_df_standardized[continuous_vars])

# Save the standardized dataset
standardized_file_path = "/mnt/data/standardized_housing_data.csv"
housing_df_standardized.to_csv(standardized_file_path, index=False)

# Display the standardized dataset to the user
import ace_tools as tools
tools.display_dataframe_to_user(name="Standardized Housing Dataset", dataframe=housing_df_standardized)
