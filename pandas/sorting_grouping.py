# groupby operation allows us to group specific data
import pandas as pd

example_data = pd.read_csv('example.csv')
print(example_data.groupby('Yes').Yes.count())  # replicates value_counts()
# groupby() created a group of Yes which alloted the same points to the given Yes
# then for each of these groups we got the Yes and counted how many times it appeared

# find the lowest value
print(example_data.groupby('Yes').Yes.min())
# each group generated is similar to a slice of a DataFrame
#   containing only data with values that match

# dataframe is accessible to us directly using the apply() method
print(example_data.groupby('Yes').apply(lambda df: df.No.iloc[0]))

print(example_data.groupby(['Yes', 'No']).apply(lambda df: df.loc[df.Yes.idxmax()]))
print(example_data.groupby(['Yes']).No.agg([len, min, max]))  # agg function allows a bunch of function usage

# multi-indexes has multiple levels
example_multi_index = example_data.groupby(['Yes', 'No']).Yes.agg([len])
print(example_multi_index)
example_multi_index.index  # converts to multi-index
print(example_multi_index)
example_multi_index.reset_index()  # resets to single index
print(example_multi_index)

# sorting
# grouping returns data in index order not value order
# the order of the rows is dependent on the values in the index not the data
# to get data in the order we want we can sort it using sort_values() method
min_yes_values = example_data.groupby('Yes').Yes.min()
min_yes_values_ordered = min_yes_values.sort_values()  # args eg. by='len', ascending=False
# sort by index values using sort_index()
min_yes_values.sort_index()
# sort by more than one column at a time
min_yes_values.sort_values(by=['No'])
