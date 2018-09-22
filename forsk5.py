#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 14:01:58 2018

@author: atuljain
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values
labels2 = dataset.iloc[:, -1].values


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor2 = LinearRegression()
regressor.fit(features, labels)
regressor2.fit(features, labels2)

labes1_bahu = regressor.predict(10)
labes2_dan = regressor2.predict(10)





