# Import seaborn for visualization
import seaborn as sns

# Generate univariate and bivariate visualizations
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Univariate Visualizations of Variables", fontsize=16, weight='bold')

# Price Distribution
sns.histplot(housing_data['Price'], kde=True, ax=axes[0, 0], bins=30, color="blue")
axes[0, 0].set_title("Price Distribution")
axes[0, 0].set_xlabel("Price")
axes[0, 0].set_ylabel("Frequency")

# SquareFootage Distribution
sns.histplot(housing_data['SquareFootage'], kde=True, ax=axes[0, 1], bins=30, color="green")
axes[0, 1].set_title("Square Footage Distribution")
axes[0, 1].set_xlabel("Square Footage")
axes[0, 1].set_ylabel("Frequency")

# CrimeRate Distribution
sns.histplot(housing_data['CrimeRate'], kde=True, ax=axes[1, 0], bins=30, color="red")
axes[1, 0].set_title("Crime Rate Distribution")
axes[1, 0].set_xlabel("Crime Rate")
axes[1, 0].set_ylabel("Frequency")

# SchoolRating Distribution
sns.histplot(housing_data['SchoolRating'], kde=True, ax=axes[1, 1], bins=30, color="purple")
axes[1, 1].set_title("School Rating Distribution")
axes[1, 1].set_xlabel("School Rating")
axes[1, 1].set_ylabel("Frequency")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

# Bivariate visualizations
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle("Bivariate Visualizations of Variables with Price", fontsize=16, weight='bold')

# Price vs Square Footage
sns.scatterplot(x='SquareFootage', y='Price', data=housing_data, ax=axes[0], color="blue")
axes[0].set_title("Price vs Square Footage")
axes[0].set_xlabel("Square Footage")
axes[0].set_ylabel("Price")

# Price vs Crime Rate
sns.scatterplot(x='CrimeRate', y='Price', data=housing_data, ax=axes[1], color="green")
axes[1].set_title("Price vs Crime Rate")
axes[1].set_xlabel("Crime Rate")
axes[1].set_ylabel("Price")

# Price vs School Rating
sns.scatterplot(x='SchoolRating', y='Price', data=housing_data, ax=axes[2], color="red")
axes[2].set_title("Price vs School Rating")
axes[2].set_xlabel("School Rating")
axes[2].set_ylabel("Price")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
