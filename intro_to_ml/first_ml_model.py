# Selecting data for modeling
# To choose variables/columns for modeling list all the columns
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

music_file_path = 'music.csv'
music_data = pd.read_csv(music_file_path)
print(music_data.columns)
music_data = music_data.dropna(axis=0)  # drop na drops missing values (think of na as "not available")
# Main ways to select subsets of the dataset are
#     1. Dot notation which we use to select the "prediction target"
#     2. Selecting with a column list which we use to select the "features"

# Selecting the prediction target
# You can pull out a variable with dot-notation
# This column is stored in a series which is broadly like a dataframe with a single column of data
# we use the dot notation to select the column we want to predict
# which is called the prediction target by convention the prediction target is also called y
# y = music_data.example_column
y = music_data['song.key']
print(y)

# Feature columns are inputted into our model (and later used to make predictions) are called features
# Eg. columns that can probably be used to make a prediction on song.key
# by convention this data is called X
music_features = ['song.duration', 'song.year', 'song.loudness', 'song.hotttnesss']
X = music_data[music_features]
print(X.describe())
# head shows the top few rows
print(X.head)

# Building your model
# you will use the scikit-learn library to create your models
# library is written as sklearn
# scikit-learn is the most popular library for modeling the types of data usually stored in DataFrames
# Model steps:
#     Define: What type of model will it be? A decision tree? Some other type of model?
#     Fit: Capture patterns from provided data. This is the heart of modeling.
#     Predict: Just what it sounds like
#     Evaluate: Determine how accurate the model's predictions are

# Define model. Specify a number for random_state to ensure same results each run
music_model = DecisionTreeRegressor(random_state=1)

# Fit model
music_model.fit(X, y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(music_model.predict(X.head()))
