# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 15:06:00 2021

@author: Mingze Gong (Rouch MacTavish)
"""

from signal2img_And_resample import signalResample, signal2image_noodles
import math
import numpy as np
import pywt
import matplotlib.pyplot as plt


def wl_filtering (signal): 
    index=[]
    data=[]
    coffs=[]
    
    for i in range(len(signal)-1):
        X=float(i)
        Y=float(signal[i])
        index.append(X)
        data.append(Y)
    #create wavelet object and define parameters
    w=pywt.Wavelet('db2')
    maxlev=pywt.dwt_max_level(len(data),w.dec_len)
    threshold=0  #Threshold for filtering
    
    #Decompose into wavelet components,to the level selected:
    coffs=pywt.wavedec(data,'db2',level=maxlev) 
    
    for i in range(1,len(coffs)):
        coffs[i]=pywt.threshold(coffs[i],threshold*max(coffs[i]))
    
    datarec=pywt.waverec(coffs,'db2')
    
    return datarec

def wp_decomposition (signal):
    """
    ['haar','db', 'sym', 'coif', 'bior', 'rbio', 'dmey', 'gaus', 'mexh', 'morl',
     'cgau', 'shan', 'fbsp', 'cmor']
    """
    wp = pywt.WaveletPacket(data=signal, wavelet='db2',mode='symmetric',maxlevel=4)
    wp_level2 = []
    wp_level4 = []
    
    level2_list = ['aa', 'ad', 'dd', 'da']
    level4_list = ['aaaa', 'aaad', 'aadd', 'aada', 'adda', 'addd', 'adad', 'adaa', 'ddaa', 
                   'ddad', 'dddd', 'ddda', 'dada', 'dadd', 'daad', 'daaa']
    level6_list = ['aaaaaa', 'aaaaad', 'aaaadd', 'aaaada', 'aaadda', 'aaaddd', 'aaadad', 
                   'aaadaa', 'aaddaa', 'aaddad', 'aadddd', 'aaddda', 'aadada', 'aadadd', 
                   'aadaad', 'aadaaa', 'addaaa', 'addaad', 'addadd', 'addada', 'adddda', 
                   'addddd', 'adddad', 'adddaa', 'adadaa', 'adadad', 'adaddd', 'adadda', 
                   'adaada', 'adaadd', 'adaaad', 'adaaaa', 'ddaaaa', 'ddaaad', 'ddaadd', 
                   'ddaada', 'ddadda', 'ddaddd', 'ddadad', 'ddadaa', 'ddddaa', 'ddddad', 
                   'dddddd', 'ddddda', 'dddada', 'dddadd', 'dddaad', 'dddaaa', 'dadaaa', 
                   'dadaad', 'dadadd', 'dadada', 'daddda', 'dadddd', 'daddad', 'daddaa', 
                   'daadaa', 'daadad', 'daaddd', 'daadda', 'daaada', 'daaadd', 'daaaad', 
                   'daaaaa']
    
    for i in range (0, len(wp.get_level(2, 'freq'))):
        wp_level2.append (wp[level2_list[i]].data)
    for i in range (0, len(wp.get_level(4, 'freq'))):
        wp_level4.append (wp[level4_list[i]].data)
    
    
    return wp_level2, wp_level4






