# Decision tree models are the basic building block of Machine Learning
# Eg.
#       Sample Decision Tree
#           Does House have more than 2 bedrooms?
#       / No                                        \ Yes
#  Predicted Price: 178000                      Predicted Price: 188000

# We use data to decide how to break the houses into two groups,
# and then again to determine the predicted price in each group.
# This step of capturing patterns from data is called fitting or training the model.
# The data used to fit the model is called the training data.
# After the model has been fit you can apply it to new data to predict prices of additional homes

# You can capture more factors of price for example by using a tree that has more "splits"
# Those are called "deeper" trees
# Eg.
#       Sample Deeper Decision Tree
#       Sample Decision Tree
#           Does House have more than 2 bedrooms?
#       / No                                        \ Yes
#  Lot Size larger than 8500 square feet         Lot size larger than 11500 square feet
#   / No                          \ Yes                     / No                           \ Yes
# Predicted Price: 146000   Predicted Price: 188000  Predicted Price: 170000  Predicted Price: 233000
# Point at the bottom of the tree that makes the prediction is called a leaf
