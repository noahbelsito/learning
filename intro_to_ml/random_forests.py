# Deep trees with lots of leaves will over fit because each prediction is coming from historical data from a few values
# Shallow trees will perform poorly because it fails to capture as many distinctions in the raw data
# Random forest uses many trees and it can make a prediction by averaging out the predictions of each component tree
# these random forests are usually considerably more accurate than most single tree models

import pandas as pd

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

music_csv = "music.csv"
music_data = pd.read_csv(music_csv)
music_data = music_data.dropna(axis=0)
y = music_data["artist.familiarity"]
features = ["artist.hotttnesss", "song.bars_confidence", "song.duration", "song.hotttnesss", "song.key_confidence", "song.loudness", "song.tempo", "song.time_signature"]
X = music_data[features]
train_X, val_X, train_y, val_y = train_test_split(X, y)

no_split_model = DecisionTreeRegressor(random_state=1)
no_split_model.fit(X, y)
no_split_predictions = no_split_model.predict(X)
print("No Split Model: ", mean_absolute_error(y, no_split_predictions))

tree_model = DecisionTreeRegressor(random_state=1)
tree_model.fit(train_X, train_y)
tree_predictions = tree_model.predict(val_X)
print("Tree Model: ", mean_absolute_error(val_y, tree_predictions))

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
forest_predictions = forest_model.predict(val_X)
print("Forest Model: ", mean_absolute_error(val_y, forest_predictions))
