#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 15:09:56 2018

@author: atuljain
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv('bluegills.csv')
features = dataset.iloc[:, 0].values
labels = dataset.iloc[:, -1].values
features = np.array(features).reshape(-1, 1)
labels = np.array(labels).reshape(-1,1)

from sklearn.linear_model import LinearRegression 
lin_reg = LinearRegression()
lin_reg.fit(features, labels)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
features_poly = poly_reg.fit_transform(features)
poly_reg.fit(features_poly, labels)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)

print"Predicting results with Linear Regression",
print lin_reg.predict(5)

print "Predicting results with Polynomial Regression",
print lin_reg_2.predict(poly_reg.fit_transform(5))

linear_score = lin_reg.score(features, labels)

poly_score = lin_reg_2.score(features_poly,labels)


plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg.predict(features), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('age')
plt.ylabel('length')
plt.show()


plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_2.predict(poly_reg.fit_transform(features)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('age')
plt.ylabel('length')
plt.show()


features_grid = np.arange(min(features), max(features), 0.1)
features_grid = features_grid.reshape(-1, 1)
plt.scatter(features, labels, color ='red')
plt.plot(features_grid, lin_reg_2.predict(poly_reg.fit_transform(features_grid)), color = 'blue')
plt.title('Truth or Bluff(Polynomial Regression)')
plt.xlabel('age')
plt.ylabel('length')
plt.show()
