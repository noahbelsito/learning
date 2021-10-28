import pandas as pd

example_data = pd.read_csv('example.csv')

# summary functions are used to summarize data
print(example_data.describe())
print(example_data.Yes.mean())  # mean of values in column
print(example_data.Yes.median())  # median of values in column
print(example_data.No.unique())  # how many unique values
print(example_data.Yes.value_counts())  # how often values occur
print(example_data.head())  # first few rows

# a map is a function that takes one set of values and "maps" them to another set of values
# this is used to transform data or create new representations from existing data
example_yes_mean = example_data.Yes.mean()
print(example_data.Yes.map(lambda p: p - example_yes_mean))  # map returns a new series where all values are transformed


def remean(row):
    row.Yes = row.Yes - example_yes_mean
    return row


# apply transforms a whole dataframe
example_data.apply(remean, axis='columns')

example_data['String1'] = ['Hello', 'Hello,']
example_data['String2'] = ['World!', 'World!']
print(example_data)
print(example_data.String1 + " " + example_data.String2)
