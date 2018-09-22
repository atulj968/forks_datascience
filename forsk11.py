#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 14:45:22 2018

@author: atuljain
"""

import numpy as np
import pandas as pd

dataset = pd.read_csv('affairs.csv')
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values

lables = np.array(labels).reshape(1,-1)

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features=[6,7])
features = onehotencoder.fit_transform(features).toarray()


from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

from sklearn.linear_model import LogisticRegression 
classifier = LogisticRegression(random_state = 0)
classifier.fit(features_train, labels_train)

#predicting the test set result
labels_pred = classifier.predict(features_test)

#making the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

x = np.array([0,0,0,1,0,0,0,1,0,0,0,0,3,25,3,1,4,16]).reshape(1,-1)

#score
classifier.score = classifier.score(features, labels)

