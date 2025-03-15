# Create a DataFrame for explained variance of each principal component
variance_df = pd.DataFrame({
    "Principal Component": [f"PC{i+1}" for i in range(len(explained_variance))],
    "Explained Variance": explained_variance,
    "Cumulative Variance": np.cumsum(explained_variance)
})

# Display the variance of each principal component
tools.display_dataframe_to_user(name="Variance of Principal Components", dataframe=variance_df)
