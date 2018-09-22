#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:11:07 2018

@author: atuljain
"""

import numpy as np
import pandas as pd


data = pd.read_csv('Social_Network_Ads copy.csv')
features = data.iloc[:, 2:-1].values
labels = data.iloc[:, -1].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler 
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.fit_transform(features_test)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5, p=2)
classifier.fit(features_train, labels_train)

pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, pred)

