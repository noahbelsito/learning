# Data type for a column in a DataFrame or a Series is known as the dtype
# You can use the dtype property to grab the type of a specific column
import pandas as pd
example_data = pd.read_csv('example.csv')

# dtype
print(example_data.Yes.dtype)

# you can convert datatypes by using astype() function
print(example_data.Yes.astype('float64').dtype)

# A DataFrame or Series index has it's own dtype
print(example_data.index.dtype)

# missing data is entries that have missing values (NaN short for "Not a Number")
# you can select NaN entries pd.isnull() or pd.notnull() for the opposite
print(pd.isnull(example_data.Yes))

# you can fill NaN values with a value using fillna()
print(example_data.Yes.fillna(0))

# you can also use replace() method to replace values in a dataframe
print(example_data.Yes.replace(21, 24))
