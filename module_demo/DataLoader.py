# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 10:41:02 2021

@author: Mingze Gong (Rouch MavTavish)
"""
import numpy as np
import os
import utils
import cv2 
import torch
import torchvision.transforms as transforms


class ImgDataset(torch.utils.data.Dataset) :
    def __init__ (self, path, transform=None) :
        self.path = path
        self.seqs = os.listdir(self.path)
        self.transform = transform
        
    def __len__ (self) :
        return (len(self.seqs))
    
    def __getitem__ (self, index) :
        seq_index = self.seqs[index]
        seq_path = os.path.join(self.path, seq_index)
        seq = np.load(seq_path)
        label = int(seq_path.split("label_")[1].split(".npy")[0])
        img = utils.signal2image_noodles(seq)
        if self.transform is not None:
            img = self.transform(img)

        return img, label
    
    
def trainLoader (path) :
    transform = transforms.Compose([
    transforms.ToTensor(),
    ])
    dataset = ImgDataset(path, transform)
    train_iter = torch.utils.data.DataLoader(dataset, batch_size=2, shuffle=False, num_workers=0)
    return train_iter


def testLoader (path) :
    transform = transforms.Compose([
    transforms.ToTensor(),
    ])
    dataset = ImgDataset(path, transform)
    test_iter = torch.utils.data.DataLoader(dataset, batch_size=2, shuffle=False, num_workers=0)
    return test_iter


array = np.load("E:\中科院深圳SIAT\projects\EEG Classification\data\labeled\label_0.npy")
print (array)

path = "E:\\中科院深圳SIAT\\projects\\EEG Classification\\data\\labeled"
train_iter = trainLoader(path)

for i, data0 in enumerate(train_iter, 0) :
    inputs, labels = data0 
    print ("input: ", inputs)
    print ("labels: ", labels)
    
    
    

