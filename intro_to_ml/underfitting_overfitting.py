# https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html
# shows the options for setting the DecisionTreeRegressor model
# it's uncommon for a model to have more than ten splits
# more splits will mean it will make better predictions on old data
#     but worse predictions on new data because it was fit too closely to specific data
#     this is called overfitting where a model matches the training data perfectly but does poor in validation
# less spits or a shallow tree don't divide data into distinct groups
#     at an extreme the resulting predictions will be far off for most data
#     even for the training data and validation
#     when a model fails to capture important distinctions and patterns in the data it performs poorly
#     this is called underfitting
# DTR validation curves shows the way models typically fit based on the amount of depth a model has
# DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
#     max_leaf_nodes is a argument for the model that provides a way to control overfitting if a model is given
#     a lot of options to create depth
# You can test a bunch of different max_leaf_nodes models using a for loop
#  for max_leaf_nodes in [5, 50, 500, 5000]:
#     my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
#     print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))

# You don't need the validation data after you've decided on a model
# The model will fit better after you've decided the best choices for the model using validation

""" Summary
    Overfitting: capturing spurious patterns that won't recur in the future, leading to less accurate predictions, or
    Underfitting: failing to capture relevant patterns, again leading to less accurate predictions.
"""
