from sklearn.model_selection import train_test_split

# Select the top 6 principal components based on E2 results
num_components_to_retain = 6
pca_selected_df = pca_df.iloc[:, :num_components_to_retain]

# Add the target variable (Price) back to the dataset
pca_selected_df["Price"] = housing_df_standardized["Price"]

# Split the dataset into training (80%) and testing (20%)
train_df, test_df = train_test_split(pca_selected_df, test_size=0.2, random_state=42)

# Save the datasets
train_file_path = "/mnt/data/pca_train_data.csv"
test_file_path = "/mnt/data/pca_test_data.csv"
train_df.to_csv(train_file_path, index=False)
test_df.to_csv(test_file_path, index=False)

# Display the training dataset
tools.display_dataframe_to_user(name="PCA Training Dataset", dataframe=train_df)
