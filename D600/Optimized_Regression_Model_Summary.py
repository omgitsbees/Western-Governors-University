import statsmodels.api as sm
from sklearn.preprocessing import LabelEncoder

# Encode categorical variables ('Garage' and 'Fireplace') for regression analysis
label_encoder = LabelEncoder()
encoded_data = new_train_data.copy()
encoded_data['Garage'] = label_encoder.fit_transform(encoded_data['Garage'])
encoded_data['Fireplace'] = label_encoder.fit_transform(encoded_data['Fireplace'])

# Separate independent variables (X) and the dependent variable (y)
X = encoded_data.drop(columns=['IsLuxury'])
y = encoded_data['IsLuxury']

# Add a constant to the independent variables for the regression model
X = sm.add_constant(X)

# Perform logistic regression using statsmodels
logit_model = sm.Logit(y, X).fit()

# Extract model parameters (AIC, BIC, pseudo R2, coefficients, and p-values)
model_summary = logit_model.summary2()

# Display the summary for review
tools.display_dataframe_to_user(name="Optimized Regression Model Summary", dataframe=model_summary.tables[1])

# Extract AIC, BIC, and pseudo R2
aic = logit_model.aic
bic = logit_model.bic
pseudo_r2 = 1 - logit_model.llf / logit_model.llnull

aic, bic, pseudo_r2
