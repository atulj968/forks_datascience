#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:06:47 2018

@author: atuljain
"""

import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0, 50.0, 10000)
plt.hist(50)
plt.show()
print (incomes.std())
print (incomes.var())