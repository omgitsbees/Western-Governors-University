from sklearn.decomposition import PCA

# Perform PCA
pca = PCA()
principal_components = pca.fit_transform(housing_df_standardized[continuous_vars])

# Convert PCA results into a DataFrame
pca_df = pd.DataFrame(principal_components, columns=[f"PC{i+1}" for i in range(len(continuous_vars))])

# Display the matrix of all principal components
tools.display_dataframe_to_user(name="Principal Components Matrix", dataframe=pca_df)
