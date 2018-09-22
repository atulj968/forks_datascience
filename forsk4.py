#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 15:40:24 2018

@author: atuljain
"""

import pands as pd
data = pd.read_csv("Cricket_Salary_Data.csv")
features = data.iloc[:, :-1].vlaues
labels = data.iloc[:, -1].values

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(features[:, 1:2])
features[:, 1:2] = imputer.tranform(features[:, 1:2])

