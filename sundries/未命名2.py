# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 14:32:54 2021

@author: Mingze Gong
"""
import math
import numpy as np
import cv2
import matplotlib.pyplot as plt
from mne.io import concatenate_raws, read_raw_edf
import mne
import os

path = "./data/"
file_list = []
for (root , dirs , files ) in os.walk (path):
    for file in files:
        file = str(root) + '/' + str(file)
        file_list.append(file)

print (file_list)

output_path = './data/labeled'
stride = 50175

raw=read_raw_edf(file_list[0], preload=False)
raw.load_data()
raw_filtered = raw.copy().filter(l_freq=5, h_freq=400)
#raw_filtered = raw.copy()
eeg = raw_filtered.to_data_frame()

eeg = list(eeg.values[:,1])
eeg = np.array(eeg)
i=0

while (i < len(eeg)):
    print (str(i) + "/" + str(len(eeg)))
    if (i+stride > len(eeg)):
        cache = eeg[i:]
        for i in range (len(cache), stride):
            cache.append(0)
        filename = str(output_path) + '/end.npy'
        np.save(filename, cache)
        break
    else:
        cache = eeg[i:i+stride]
        filename = str(output_path) + '/' + str(i) + '.npy'
        np.save(filename, cache)
        i = i + stride + 1
        



