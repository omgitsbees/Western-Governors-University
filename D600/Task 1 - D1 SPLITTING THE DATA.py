from sklearn.model_selection import train_test_split

# Splitting the dataset into training and testing datasets (80% train, 20% test)
train_data, test_data = train_test_split(housing_data, test_size=0.2, random_state=42)

# Save the training and testing datasets as CSV files
train_file_path = '/mnt/data/housing_train_dataset.csv'
test_file_path = '/mnt/data/housing_test_dataset.csv'

train_data.to_csv(train_file_path, index=False)
test_data.to_csv(test_file_path, index=False)

train_file_path, test_file_path
