from sklearn.metrics import confusion_matrix, accuracy_score

# Predict probabilities and classify predictions based on a threshold of 0.5
train_predictions = logit_model.predict(X)
train_predicted_classes = (train_predictions >= 0.5).astype(int)

# Compute the confusion matrix and accuracy
conf_matrix = confusion_matrix(y, train_predicted_classes)
accuracy = accuracy_score(y, train_predicted_classes)

conf_matrix, accuracy
