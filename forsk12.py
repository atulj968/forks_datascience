#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 14:32:59 2018

@author: atuljain
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('mushrooms.csv')
features = data.iloc[:,[5,-2,-1]].values
labels = data.iloc[:,1:2].values
features = np.asarray(features)

from sklearn.preprocessing import LabelEncoder, OneHotEnoder
labelencoder = LabelEncoder()
features = 

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = .25, random_state = 0)


 from sklearn.neighbors import KNeighborsClassifier 
 knc = KNeighborsClassifier(n_neighbors=5, p=2)
 knc.fit(features_train, label_train)
 
 pred = knc.predict(features_test)
 