#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 15:36:57 2018

@author: atuljain
"""

import numpy as np
import pandas as pd

dataset = pd.read_csv('iq_size.csv')
features = dataset.iloc[:, 1:].values
labels = dataset.iloc[:, 0:1].values



from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)




from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)



Pred = regressor.predict(features_test)


score = regressor.score(features_train, labels_train)
print(score)

val = np.array([90,70,150]).reshape(1,-1)
new_pred = regressor.predict(val)