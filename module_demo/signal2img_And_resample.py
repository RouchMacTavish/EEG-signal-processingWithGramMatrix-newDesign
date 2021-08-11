# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 14:58:36 2021

@author: Mingze Gong (Rouch MacTavish)
"""
import numpy as np
import math


def signal2image_sequential (signal):
    signal_sum = float(sum(signal))
    norm = []
    for i in range (0,len(signal)):
        norm.append(255 * float(signal[i]) / signal_sum)

    L = math.floor(math.sqrt(len(signal))+ 1)
    image = np.zeros(shape=(L,L))
    count = 0
    for i in range (0,L):
        if count < len(signal):
            for j in range (0,L):
                image[i][j] = norm[count]
                count = count + 1
                if count >= len(signal):
                    break

    return image


def signal2image_noodles (signal):
    # updated on 20210726
    signal_sum = float(sum(signal))
    sig = []
    for i in range (0,len(signal)):
        sig.append(255 * float(signal[i]) / signal_sum)
    L = math.floor(math.sqrt(len(sig))+ 1)
    img = np.zeros (shape=(L,L))
    count = 0
    
    for i in range (0,L):
        if count < len(sig):
            if ((i+1) % 2 == 1):
                for j in range (0,L):
                    img[i][j] = sig[count]
                    count = count + 1
                    if count >= len(sig):
                        break
            elif ((i+1) % 2 == 0):
                j = L-1
                while (j >= 0): 
                    img[i][j] = sig[count]
                    count = count + 1
                    j = j - 1
                    if count >= len(sig):
                        break
    return img


def signalResample (signal, stride):
    new_signal = np.zeros([1,1], dtype=float)
    i = 0
    
    while (i<len(signal)):
        new_signal = np.append(new_signal, signal[i])
        i = i + stride
        print ("Sampleing-----> " + str(i) + " \\ " + str(len(signal)))

    print ("Successfully Resampling ! ! !")
    return new_signal