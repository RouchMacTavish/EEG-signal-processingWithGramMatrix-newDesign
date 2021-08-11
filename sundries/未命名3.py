# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:45:22 2021

@author: 94383
"""


import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn import preprocessing
import torch
import cv2

def dotRedefined (a, b):
    return np.cos(a+b)

def dot (a, b):
    return np.cos(a+b)
array = np.random.randint(0,100,512)

angles = []
radius = []
cache = []
Gram = []
for i in range(0, len(array)):
    cache.append (array[i]/(i+1))
    
cache = ( (cache-np.min(cache)) + (cache-np.max(cache)) ) / (np.max(cache) - np.min(cache))
    
for i in range (len(array)):
    angles.append (np.arccos(cache[i]))
    radius.append ( math.sqrt( pow(i, 2) + pow(array[i], 2) ) )
for i in range(len(angles)):
    cache2 = []
    for j in range(len(angles)):
        cache2.append(dot(angles[i], angles[j]))
    Gram.append(cache2)
Gram = np.array(Gram)
cv2.imshow('test2', Gram)    
"""
array = array.reshape(-1, 1)
max_abs_scaler = preprocessing.MaxAbsScaler().fit(array)
norm = max_abs_scaler.transform(array)
norm = norm.reshape(1, -1)
norm = list(norm)
angles = []
Gram = []

for i in range (len(norm)):
    angles.append(np.arccos(norm[i]))

for i in range(len(angles[0])):
    cache = []
    for j in range(len(angles[0])):
        cache.append(dotRedefined(angles[0][i], angles[0][j]))
    Gram.append(cache)
"""

