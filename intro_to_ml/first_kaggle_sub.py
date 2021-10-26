import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

home_path = "sub_data/train.csv"
home_data = pd.read_csv(home_path)
y = home_data.SalePrice
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[features]

train_X, val_X, train_y, val_y = train_test_split(X, y)

rf_model = RandomForestRegressor(random_state=1)
rf_model.fit(train_X, train_y)
rf_val_preds = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(rf_val_preds, val_y)

print("Validation MAE for Random Forest Model: {:,.0f}".format(rf_val_mae))
# after good validation we can make a full model on the train data and test on the test data for a submission
rf_model_full = RandomForestRegressor(random_state=1)
rf_model_full.fit(X, y)

val_path = "sub_data/test.csv"
val_data = pd.read_csv(val_path)
val_X = val_data[features]
rf_val_full_preds = rf_model.predict(val_X)

# creating a file from predictions
output = pd.DataFrame({'Id': val_data.Id,
                       'SalePrice': rf_val_full_preds})
output.to_csv('sub_data/submission.csv', index=False)
