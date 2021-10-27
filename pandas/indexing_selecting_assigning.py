# Native Python objects provide good methods of indexing data
# Pandas carries all of these over
import pandas as pd

example_data = pd.read_csv('example.csv', index_col=0)
print(example_data)

# You can access a column using dot notation
print(example_data.Yes)

# Python dictionary can access it's values using the indexing operator ([])
# You can also do that with pandas
print(example_data['No'])
# [] method can index names with reserve characters such as '.' ' '
# to index a single specific value you can add another index operator ([])
print(example_data['No'][1])
# indexing operator and attribute selection are nice because they work like the rest of the python ecosystem
# pandas has it's own accessor operators (loc and iloc) for more advanced operations

# index-based selection (iloc)
print(example_data.iloc[0])  # first row
# both loc and iloc are row-first, column-second (the opposite of native python)
print(example_data.iloc[:, 0])  # first column (: meaning everything)
print(example_data.iloc[:1, 0])
print(example_data.iloc[[0, 1], 0])
print(example_data.iloc[-1:])

# label-based selection (loc)
print(example_data.loc[0, 'Yes'])
print(example_data.loc[:, ['No']])
# best used for selection when indexes are strings

# conditional selection
# operation produces a series of True / False booleans dependent on condition
print(example_data.Yes == 1)
print(example_data.loc[example_data.No == 2])  # selects relevant data
print(example_data.loc[(example_data.Yes == 21) & (example_data.No <= 90)])  # AND operator
print(example_data.loc[(example_data.Yes == 50) | (example_data.No <= 90)])  # OR operator

# isin operator
print(example_data.loc[example_data.Yes.isin([1, 21])])

# notnull operator
print(example_data.loc[example_data.No.notnull()])

# assigning data
example_data['Maybe'] = [5, 22]
print(example_data)

# or with an iterable of values
example_data['index_backwards'] = range(len(example_data), 0, -1)
print(example_data)
