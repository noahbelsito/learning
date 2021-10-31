# Approaches to dealing with missing values
# 1) Drop Columns with missing values
# 2) Imputation (filling in the missing values with some number)
# 3) An Extension To Imputation (extra column to show missing value)
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import pandas as pd

example_data = pd.read_csv('train.csv')
y = example_data.SalePrice
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = example_data[features]
train_X, val_X, train_y, val_y = train_test_split(X, y)


# Function to compare methods
def score_dataset(x_train, x_val, y_train, y_val):
    model = RandomForestRegressor(n_estimators=10, random_state=0)
    model.fit(x_train, y_train)
    preds = model.predict(x_val)
    return mean_absolute_error(y_val, preds)


# Approach 1 drop columns with missing values
cols_with_missing = [col for col in train_X.columns if train_X[col].isnull().any()]

# Drop columns in training and validation data
reduced_X_train = train_X.drop(cols_with_missing, axis=1)
reduced_X_valid = val_X.drop(cols_with_missing, axis=1)

print("MAE from Approach 1:", score_dataset(reduced_X_train, reduced_X_valid, train_y, val_y))

# Imputation
my_imputer = SimpleImputer()
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(train_X))
imputed_X_valid = pd.DataFrame(my_imputer.transform(val_X))

# Imputation removed column names; put them back
imputed_X_train.columns = train_X.columns
imputed_X_valid.columns = val_X.columns

print("MAE from Approach 2:", score_dataset(imputed_X_train, imputed_X_valid, train_y, val_y))

# Make copy to avoid changing original data (when imputing)
X_train_plus = train_X.copy()
X_valid_plus = val_X.copy()

# Make new columns indicating what will be imputed
for col in cols_with_missing:
    X_train_plus[col + '_was_missing'] = X_train_plus[col].isnull()
    X_valid_plus[col + '_was_missing'] = X_valid_plus[col].isnull()

# Imputation
my_imputer = SimpleImputer()
imputed_X_train_plus = pd.DataFrame(my_imputer.fit_transform(X_train_plus))
imputed_X_valid_plus = pd.DataFrame(my_imputer.transform(X_valid_plus))

# Imputation removed column names; put them back
imputed_X_train_plus.columns = X_train_plus.columns
imputed_X_valid_plus.columns = X_valid_plus.columns

print("MAE from Approach 3:", score_dataset(imputed_X_train_plus, imputed_X_valid_plus, train_y, val_y))
