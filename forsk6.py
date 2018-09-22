#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:22:44 2018

@author: atuljain
"""

import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Income_Data.csv')
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values

from sklearn.model_selection import train_test_split 
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

#feature salling

""" from sklearn.preprocessing import StadardScaler
sc_features = StandardScaler()
features_train = sc_features.fit_transform(features_train)
featurs_test = sc_features.tansform(features_train)
sc_labels = StanderdScaler()
lablels_train = sc_labels.fit_transform(labels_train)"""

# Fitting Simple Linear regression to the trining set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

# Predecting the Test set results
labels_pred = regressor.predict(features_test)

# Model Score
Score = regressor.score(features_test, labels_test)

# Visualising  the Training set results
plt.scatter(features_train, labels_train, color = 'red')
plt.plot(features_train, regressor.predict(features_train), color = 'blue')
plt.title('Incomes vs ML-Experience (Training set)')
plt.xlabel('ML-Experience')
plt.ylebel('Income')
plt.show()

#Visualising the test set results
plt.scatter(features_test, labels_test, color = 'red')
plt.plot(features_train, regressor.predict(features_train), color = 'blue')
plt.title('Income vs ML-Experience')
plt.xlabel('Ml-Experince')
plt.ylabel('Income')
plt.show()