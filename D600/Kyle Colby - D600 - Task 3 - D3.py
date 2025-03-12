# Generate descriptive statistics for the dependent and independent variables
descriptive_stats = housing_df_standardized[["Price"] + continuous_vars].describe().transpose()

# Display the descriptive statistics
tools.display_dataframe_to_user(name="Descriptive Statistics of Housing Data", dataframe=descriptive_stats)


