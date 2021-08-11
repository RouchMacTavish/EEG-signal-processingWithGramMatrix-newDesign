# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 09:15:31 2021

@author: Mingze Gong (Rouch MacTavish)
"""

import numpy as np
import matplotlib.pyplot as plt
import pywt
import pywt.data


#array = np.random.randint(100, size=50176)
#np.save ("test.npy", array)
array = np.load ('test.npy')
print (array)
#plt.plot(array)
print (len(array))






"""
wp = pywt.WaveletPacket(data=array, wavelet='db2',mode='symmetric',maxlevel=4)
#根据频段频率（freq）进行排序
print([node.path for node in wp.get_level(1, 'freq')])
print([node.path for node in wp.get_level(2, 'freq')])
print([node.path for node in wp.get_level(3, 'freq')])
print([node.path for node in wp.get_level(4, 'freq')])


cache = []
x = ['aaaa', 'aaad', 'aadd', 'aada', 'adda', 'addd', 'adad', 'adaa', 'ddaa', 
     'ddad', 'dddd', 'ddda', 'dada', 'dadd', 'daad', 'daaa']
for i in range (0, len(wp.get_level(4, 'freq'))):
    cache.append (wp[x[i]].data)
    
print (len(cache))
"""




