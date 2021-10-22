# Model validation measures the quality of a model
# The relative measure is the predictive accuracy of the model
# They make predictions with their training data and compare those predictions to the target values in the training data
# Metrics for summarizing model quality but we'll start with one called Mean Absolute Error
# error = actual-predicted
from first_ml_model import *
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

predicted_model = music_model.predict(X)
print("Bad example of data validation: ", mean_absolute_error(y, predicted_model))
# mean absolute error is the average amount the prediction model is off
# this is called in-sample scores
# we used a single "sample" of data for both building the model and evaluating it
# this is bad because since the pattern was derived from the training data the model will appear accurate in training
# but if the pattern doesn't hold when the model sees new data the model is inaccurate in practice
# since models practical value come from making predictions on new data
# we don't want to use data that was used to build the model
# the easiest way to do this is exclude some data from the data set
# adding it to a new data set which is called validation data
# Eg.

# split data into training and validation data for both features and targets
# split is based on a random number generator
# the random_state argument guarantees we get the same split every time
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)
# define the model
music_model_v2 = DecisionTreeRegressor()
# Fit model
music_model_v2.fit(train_X, train_y)
# Validate model
# get predicted prices on validation data
val_predictions = music_model_v2.predict(val_X)
print("Better example using split data: ", mean_absolute_error(val_y, val_predictions))
# This is the difference between a model that seems right but doesn't work in practical use
# You can improve models by experimenting with different features or model types
