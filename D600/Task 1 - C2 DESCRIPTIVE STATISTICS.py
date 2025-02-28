# Calculating descriptive statistics for the dependent and independent variables
variables_to_describe = ['Price', 'SquareFootage', 'CrimeRate', 'SchoolRating']
descriptive_stats = housing_data[variables_to_describe].describe().T

# Adding additional statistics: Mode
mode_stats = housing_data[variables_to_describe].mode().iloc[0]
descriptive_stats['Mode'] = mode_stats

# Adding Range
descriptive_stats['Range'] = descriptive_stats['max'] - descriptive_stats['min']

# Displaying the descriptive statistics to the user
import ace_tools as tools; tools.display_dataframe_to_user(name="Descriptive Statistics for Variables", dataframe=descriptive_stats)
