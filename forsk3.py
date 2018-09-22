#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 15:08:00 2018

@author: atuljain
"""

import pandas as pd
data = pd.read_csv("Cricket_2017.csv")
features = data.iloc[:, :-1].values
labels = data.iloc[:, -1].vlaues

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder = LabelEncoder()
features[:,0] = labelencoder.fit_transform(features[:,0])
features[:,1] = labelencoder.fit_trasform(features[:,1])

onehotencoder = OneHotEncoder(categorical_features=[0,1])
features = onehotencoder.fit_transform(features).toarry()

labels = onehotencoder.fit_tansform(labels)

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)

