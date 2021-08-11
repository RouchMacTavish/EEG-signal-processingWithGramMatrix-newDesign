# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 15:00:12 2021

@author: Mingze Gong (Rouch MacTavish)
"""

import numpy as np
import time 
from signal2img_And_resample import signalResample
from mne.io import concatenate_raws, read_raw_edf

def signalStorage_local (path, low_freq=1, high_freq=60, resample_stride=25):
    signal = read_raw_edf (path, preload=False)
    signal.load_data()
    signal_filtered = signal.copy().filter(l_freq=low_freq, h_freq=high_freq)
    signal = signal_filtered.to_data_frame()
    
    channels = [3,4,7] #ECG, EMG, EEG
    data_list = []
    
    for channel in channels:
        data = list(signal.values[:,channel])
        data = np.array(data)
        data = signalResample(data, stride=resample_stride)
        data_list.append(data)
    
    localtime = time.localtime(time.time())
    filename = 'Data_' + (str(localtime[0]) + str(localtime[1]) + str(localtime[2]) + str(localtime[3]) + str(localtime[4]))
    np.save(filename ,data_list)
    print ("Successfully Transformation !!!")
    
    return filename