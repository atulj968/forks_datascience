#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:07:54 2018

@author: atuljain
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



dataset = pd.read_csv('PastHires.csv')
features = dataset.iloc[:,:-1] .values 
labels = dataset.iloc[:, -1].values

features = np.array(labels).reshape(-1,1)

from sklearn.preprocessing import LabelEncoder , OneHotEncoder
labelencoder = LabelEncoder()
features[:,1] = labelencoder.fit_transform(features[:,1])
features[:,3] = labelencoder.fit_transform(features[:,3])
features[:,4] = labelencoder.fit_transform(features[:,4])
features[:,5] = labelencoder.fit_transform(features[:,5])

onehotencoder = OneHotEncoder(categorical_features=[1,3,4,5])
features = onehotencoder.fit_transform(features).toarray()

labels[:,0] = labelencoder.fit_transform(labels[:,0])
onehotencoder = OneHotEncoder(categorical_features=[0])
labels = onehotencoder.fit_transform(labels).toarray()

from sklearn.tree import DecisionTreeRegressor as dtr
prog = dtr(random_state = 0)
prog.fit(features,labels)

a = np.array([0,1,1,0,0,0,1,0,1,10,4]).reshape(1,-1)


pred = prog.predict(a)

features_grid = np.arange(min(features), max(features), 0.01)
features_grid = features_grid.reshape((len(features_grid)), 1)
plt.scatter(features, labels, color = 'red')
plt.plot(features_grid, prog.predict(features_grid), color='blue')
plt.title('Hire or Not Hire(Decision type Regression)')
plt.xlabel('Year of experience')
plt.ylabel('Hire')
plt.show()