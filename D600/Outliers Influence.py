from statsmodels.stats.outliers_influence import variance_inflation_factor
import numpy as np

# Verify multicollinearity (VIF) for independent variables
vif_data = pd.DataFrame()
vif_data["Variable"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

# Check linearity assumption via partial residual plots for key predictors
# Generate partial residual plots for a selected subset of predictors
linearity_check_plots = []
for predictor in ['SquareFootage', 'NumBathrooms', 'NumBedrooms']:
    plt.figure(figsize=(8, 5))
    sm.graphics.plot_partregress(endog='IsLuxury', exog_i=predictor, exog_others=X.drop(columns=[predictor]), data=encoded_data, obs_labels=False)
    plt.title(f"Partial Residual Plot: {predictor}")
    plt.xlabel(predictor)
    plt.ylabel('Partial Residuals')
    plt.tight_layout()
    plt.show()

# Output VIF data to check multicollinearity
tools.display_dataframe_to_user(name="Variance Inflation Factor (VIF) for Independent Variables", dataframe=vif_data)
