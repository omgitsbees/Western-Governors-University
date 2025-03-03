# Simplify output: Save the optimized model's key metrics as text for clarity
optimized_model_summary = {
    "Adjusted R2": optimized_model.rsquared_adj,
    "R2": optimized_model.rsquared,
    "F-statistics": optimized_model.fvalue,
    "Probability F-statistics": optimized_model.f_pvalue,
    "Coefficients": optimized_model.params.to_dict(),
    "P-values": optimized_model.pvalues.to_dict()
}

# Write the summary to a text file
optimized_summary_file = '/mnt/data/optimized_model_summary.txt'
with open(optimized_summary_file, 'w') as file:
    for key, value in optimized_model_summary.items():
        file.write(f"{key}:\n{value}\n\n")

optimized_summary_file
