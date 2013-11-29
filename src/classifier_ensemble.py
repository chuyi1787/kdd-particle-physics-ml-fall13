#!/usr/bin/python2

# This is an ensemble of good classifiers, meant to vote on some set of
# training data.
# Random Forest
# Extra Random Forest
# Logistic Regression
# AdaBoost
# GradientBoost
# Majority vote wins.

import sys

import adaboost
import extra_randomized_trees
import gradient_boost
import random_forest
import logistic_regression

from util import write_test_prediction, load_validation_data
from metrics import acc

import numpy as np

if __name__ == "__main__":
    # First obtain our training and testing data
    Xt, Yt, Xv = load_validation_data()

    # Now, we train each classifier on the training data
    classifiers = [
            adaboost.train(Xt, Yt),
            extra_randomized_trees.train(Xt, Yt),
            gradient_boost.train(Xt, Yt),
            random_forest.train(Xt, Yt),
            logistic_regression.train(Xt, Yt)]

    # Predict and vote
    predictions = [c.predict(Xv) for c in classifiers]
    majority = []
    for data_index in range(Xv.shape[0]):
        vote = round(sum([p[data_index] for p in predictions])/5.0)
        majority.append(vote)

    # Final accuracy
    write_test_prediction("out.txt", np.array(majority))
