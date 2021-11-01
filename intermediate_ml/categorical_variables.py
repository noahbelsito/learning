# A categorical variable takes only a limited number
# Consider a survey that asks how often you eat
#   eg. Four options: "Never", "Rarely", "Most days", or "Every day"
#   falls into a fixed set of categories
# You will get error if you try to plug these variables into most machine learning models
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OrdinalEncoder


def score_dataset(x_train, x_val, y_train, y_val):
    model = RandomForestRegressor(n_estimators=10, random_state=0)
    model.fit(x_train, y_train)
    preds = model.predict(x_val)
    return mean_absolute_error(y_val, preds)


example_data = pd.read_csv('train.csv')
y = example_data.SalePrice
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = example_data[features]
train_X, val_X, train_y, val_y = train_test_split(X, y)

s = (train_X.dtypes == 'object')
object_cols = list(s[s].index)

# 1) Drop Categorical Variables
#   The easiest approach to dealing with categorical variables is to simply remove them from the dataset
drop_X_train = train_X.select_dtypes(exclude=['object'])
drop_X_valid = val_X.select_dtypes(exclude=['object'])

print("MAE from Approach 1 (Drop categorical variables):")
print(score_dataset(drop_X_train, drop_X_valid, train_y, val_y))

# 2) Ordinal Encoding
#   Assigns each unique value to a different integer
# Make copy to avoid changing original data
label_X_train = train_X.copy()
label_X_valid = val_X.copy()

# Apply ordinal encoder to each column with categorical data
ordinal_encoder = OrdinalEncoder()
label_X_train[object_cols] = ordinal_encoder.fit_transform(train_X[object_cols])
label_X_valid[object_cols] = ordinal_encoder.transform(val_X[object_cols])

print("MAE from Approach 2 (Ordinal Encoding):")
print(score_dataset(label_X_train, label_X_valid, train_y, val_y))

# 3) One-Hot Encoding
#   creates new columns indicating the presence (or absence) of each possible value in the original data
# Apply one-hot encoder to each column with categorical data
OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(train_X[object_cols]))
OH_cols_valid = pd.DataFrame(OH_encoder.transform(val_X[object_cols]))

# One-hot encoding removed index; put it back
OH_cols_train.index = train_X.index
OH_cols_valid.index = val_X.index

# Remove categorical columns (will replace with one-hot encoding)
num_X_train = train_X.drop(object_cols, axis=1)
num_X_valid = val_X.drop(object_cols, axis=1)

# Add one-hot encoded columns to numerical features
OH_X_train = pd.concat([num_X_train, OH_cols_train], axis=1)
OH_X_valid = pd.concat([num_X_valid, OH_cols_valid], axis=1)

print("MAE from Approach 3 (One-Hot Encoding):")
print(score_dataset(OH_X_train, OH_X_valid, train_y, val_y))
