# Pandas is the primary tool data scientists use for exploring and manipulating data
# pd is common practice
import pandas as pd

# DataFrames are the most important part of pandas
# DataFrames can be considered tables similar to an excel spreadsheet or SQL table
music = 'music.csv'
music_data = pd.read_csv(music)
print(music_data.describe())

# The results from describe show 8 numbers for each column in the dataset
# The first is the count it shows how many rows have non-missing values
#     Missing values arise for a bunch reasons
# The second is the mean which is the average
# Third is standard deviation which measures how numerically spread out the values are
# min, 25, 50, 75, max are the quartile ranges
