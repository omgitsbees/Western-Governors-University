import matplotlib.pyplot as plt
import seaborn as sns

# Set up the visual style
sns.set(style="whitegrid")

# Plot univariate visualizations for each independent variable
for column in variables[1:]:  # Skip 'IsLuxury' for now
    plt.figure(figsize=(8, 5))
    if selected_data[column].dtype == 'object':  # For categorical variables
        sns.countplot(data=selected_data, x=column, palette="viridis")
    else:  # For numerical variables
        sns.histplot(selected_data[column], kde=True, bins=30, color="blue")
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# Bivariate visualizations for dependent vs. independent variables
for column in variables[1:]:
    plt.figure(figsize=(8, 5))
    if selected_data[column].dtype == 'object':  # Categorical independent variables
        sns.countplot(data=selected_data, x=column, hue="IsLuxury", palette="viridis")
    else:  # Numerical independent variables
        sns.boxplot(data=selected_data, x="IsLuxury", y=column, palette="viridis")
    plt.title(f"{column} vs. IsLuxury")
    plt.xlabel(column)
    plt.ylabel("Value")
    plt.tight_layout()
    plt.show()
