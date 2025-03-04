from sklearn.metrics import mean_squared_error

# Predict the training set values using the optimized model
X_train_optimized = X_train[optimized_model.model.exog_names]  # Include only the optimized variables
y_train_pred = optimized_model.predict(X_train_optimized)

# Calculate the mean squared error (MSE) for the training set
mse_train = mean_squared_error(y_train, y_train_pred)
mse_train
