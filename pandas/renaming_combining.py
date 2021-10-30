import pandas as pd
example_data = pd.read_csv('example.csv')

# rename changes the index names and/or column names
example_data.rename(columns={'Yes': 'Affirmative'})
# you can rename index values by using index or column keywords
example_data.rename(index={0: 'firstEntry', 1: 'secondEntry'})
# usually set_index() is more convenient

# both the row index and the column index can have their own name attribute
# rename_axis() can change these names
example_data.rename_axis('Unnamed', axis='rows').rename_axis(0, axis='columns')

print(example_data)
