# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 10:16:50 2021

@author: Mingze Gong
"""

import matplotlib.pyplot as plt
import numpy as np
import math


array = np.random.randint(0, 100, 512)
time_stamp = []
for i in range(len(array)):
    time_stamp.append( i / math.sqrt(1+pow(i, 2)))

for i in range (len(array)):
    array[i] = array[i] * time_stamp[i]

#plt.plot(array)