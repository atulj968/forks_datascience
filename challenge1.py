#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:34:20 2018

@author: atuljain
"""

import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
print(incomes)
plt.hist(incomes, 50)
np.mean(incomes)
np.median(incomes)
plt.show()

