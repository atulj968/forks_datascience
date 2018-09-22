#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 14:02:08 2018

@author: atuljain
"""

import numpy as np
import pandas as pd

dataset = pd.read_csv('Salary_Classification.csv')
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1:].values


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
features[:, 0] = labelencoder.fit_transform(features[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarry()

features = features[:, 1:]


from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)


from sklearn.preprocessing import StandardScaler
sc = StandardScaler
features_train = sc.fit_transform(features_train)
features_test = sc.fit_transform(features_test)


from sklearn.preprocessing import LinearRegression
regressor = LinearRegression
regressor.fit(features_train, labels_train)



Pred = regressor.predict(features_test)


score = regressor.score(features_train, labels_train)
