# Prepare the test dataset for prediction
test_encoded_data = new_test_data.copy()
test_encoded_data['Garage'] = label_encoder.transform(test_encoded_data['Garage'])
test_encoded_data['Fireplace'] = label_encoder.transform(test_encoded_data['Fireplace'])

# Separate independent variables (X_test) and the dependent variable (y_test)
X_test = test_encoded_data.drop(columns=['IsLuxury'])
y_test = test_encoded_data['IsLuxury']

# Add a constant to the test independent variables for the regression model
X_test = sm.add_constant(X_test)

# Predict probabilities and classify predictions based on a threshold of 0.5 for the test dataset
test_predictions = logit_model.predict(X_test)
test_predicted_classes = (test_predictions >= 0.5).astype(int)

# Compute the confusion matrix and accuracy for the test dataset
test_conf_matrix = confusion_matrix(y_test, test_predicted_classes)
test_accuracy = accuracy_score(y_test, test_predicted_classes)

# Display the confusion matrix and accuracy for the test dataset
test_conf_matrix, test_accuracy
