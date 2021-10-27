# import pandas
import pandas as pd

# Two core objects in pandas are the dataframe and series
# Dataframe is a table that contains an array of individual entries each of which has a certain value
# Each entry corresponds to a row (to record) and a column
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}))
# List of row labels used in a Dataframe is known as the index
print(pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
                    'Sue': ['Pretty good.', 'Bland.']},
                   index=['Product A', 'Product B']))
# a series is a sequence of data values; if a datatable is a table a series is a list
pd.Series([1, 2, 3, 4, 5])
# a series in essence is a single column of a dataframe
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

# reading data files
example_file = pd.read_csv("../intro_to_ml/music.csv")  # you can specify index column with index_col=#
print(example_file.shape)  # shows the shape of the DataFrame
print(example_file.head())
