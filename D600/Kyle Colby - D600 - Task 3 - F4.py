# Prepare the test dataset (drop the Price column to match training features)
X_test = test_df.drop(columns=["Price"])
y_test = test_df["Price"]

# Add constant for intercept
X_test = sm.add_constant(X_test)

# Predict on the test set
y_test_pred = model.predict(X_test)

# Compute Mean Squared Error (MSE) on test set
mse_test = mean_squared_error(y_test, y_test_pred)

# Display the MSE for the test dataset
mse_test
