import matplotlib.pyplot as plt
import numpy as np

# Explained variance ratio
explained_variance = pca.explained_variance_ratio_

# Create a scree plot
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(explained_variance) + 1), explained_variance, marker='o', linestyle='--')
plt.xlabel("Principal Component")
plt.ylabel("Variance Explained")
plt.title("Scree Plot of Principal Components")
plt.axhline(y=1/len(continuous_vars), color='r', linestyle='--', label="Kaiser Rule Threshold")
plt.legend()
plt.grid()

# Show the plot
plt.show()
