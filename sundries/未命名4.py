# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 10:41:07 2021

@author: Mingze Gong (Rouch MacTavish)
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn import preprocessing
import torch


def sparseness (array):
    m,n = np.shape(array)
    N = math.sqrt(m*n)
    L1 = 0
    L2 = 0
    
    for i in range(m):
        for j in range(n):
            L1 += abs(array[i][j])
            
    for i in range(m):
        for j in range(n):
            L2 += pow(array[i][j],2)
            
    L2 = math.sqrt(L2)
    
    sparseness = (N - L1/L2) / (N-1)
    return sparseness

def dot (a, b):
    return (a[0]*b[0] + a[1]*b[1])

def dotRedefined (a, b):
    return np.cos(a+b)
"""
def reformation (array, length):
    res = []
    for i in length:
        res.
"""
def GramMatrix (array):
    Gram = []
    for i in range(0, len(array)):
        cache = []
        ref1 = [i, array[i]]
        for j in range(0, len(array)):
            ref2 = [j, array[j]]
            dot_res = dot(ref1, ref2)
            cache.append(dot_res)
        Gram.append(cache)
    return Gram

def GramMatrixRedefined (array):
    norm = ((array-np.max(array)) + (array-np.min(array))) / (np.max(array) - np.min(array))
    angles = []
    Gram = []
    
    for i in range (len(norm)):
        angles.append(np.arccos(norm[i]))
    for i in range(len(angles)):
        cache = []
        for j in range(len(angles)):
            cache.append(dotRedefined(angles[i], angles[j]))
        Gram.append(cache)
    return Gram
    
"""
array = np.array([1,2,3,4])
array = array.reshape(-1,1)
max_abs_scaler = preprocessing.MaxAbsScaler().fit(array)
norm = max_abs_scaler.transform(array)
print (norm.reshape(1, -1))
"""
count = 0
for i in range(0,1000):
    array = np.random.randint(0,10,100)
    Gram1 = GramMatrixRedefined(array)
    spar1 = sparseness(Gram1)
    Gram2 = GramMatrix(array)
    spar2 = sparseness(Gram2)
    if (spar1 > spar2):
        count += 1
    print (str(i) + "||" + str(1000))
        
print (count)
