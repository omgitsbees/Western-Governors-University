import statsmodels.api as sm

# Separate independent variables (principal components) and target variable (Price)
X_train = train_df.drop(columns=["Price"])
y_train = train_df["Price"]

# Add constant for intercept in regression model
X_train = sm.add_constant(X_train)

# Fit the multiple linear regression model
model = sm.OLS(y_train, X_train).fit()

# Extract the summary of the optimized model
model_summary = model.summary()

# Display key regression metrics
regression_results = {
    "Adjusted R2": model.rsquared_adj,
    "R2": model.rsquared,
    "F-statistic": model.fvalue,
    "Prob (F-statistic)": model.f_pvalue,
    "Coefficients": model.params.to_dict(),
    "P-values": model.pvalues.to_dict()
}

# Display the regression results
tools.display_dataframe_to_user(name="Regression Model Summary", dataframe=pd.DataFrame.from_dict(regression_results, orient='index'))

# Show the model summary text output
model_summary
