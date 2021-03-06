# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 11:46:11 2021

@author: Mingze Gong (Rouch MacTavish)
"""

import torch
import torch.nn as nn 
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms 
import argparse 
from NovelNet import NovelNet
import os 
import time 
import utils


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

epochs = 100
pre_epoch = 0
batch_size = 128
lr = 0.01

path1 = ""
path2 = ""
train_loader = utils.trainLoader(path1)
test_loader = utils.testLoader(path2)
net = NovelNet (num_classes=10).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=lr, momentum=0.9, weight_decay=1e-4) #5e-4 1e-3
best_acc = 60
print ("Start Training !")

with open ("acc.txt","w") as file1 :
    with open ("log.txt","w") as file2 :
        for epoch in range (pre_epoch, epochs) :
            print ("\nEpoch : " + str(epoch+1))
            print ("Training--->")
            net.train()
            sum_loss = 0.00
            test_loss = 0.00
            correct = 0.00
            total = 0.00
            
            for i, data in enumerate(train_loader,0) :
                length = len(train_loader)
                inputs , labels = data
                inputs , labels = inputs.to(device), labels.to(device)
                optimizer.zero_grad()
                
                outputs = net(inputs)
                loss = criterion(outputs, labels)
                loss.backward()
                optimizer.step()
                
                sum_loss += loss.item()
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += predicted.eq(labels.data).cpu().sum()
                
                print ('[epoch:%d, iter:%d] Loss: %.05f | Acc: %.3f%% |'
                       % (epoch + 1, (i + 1 + epoch * length), sum_loss / (i + 1), 100. * correct / total))
                file2.write('%03d  %05d |Loss: %.05f | Acc: %.3f%% |'
                         % (epoch + 1, (i + 1 + epoch * length), sum_loss / (i + 1), 100. * correct / total))
                file2.write("\n")
                file2.flush()
                
        
        
            print("Testing--->")
            with torch.no_grad() :
                correct = 0
                total = 0
                start_test = time.perf_counter() 
                for data in test_loader :
                    net.eval()
                    images, labels = data
                    images, labels = images.to(device), labels.to(device)
                    outputs = net(images)
                    _, predicted = torch.max(outputs.data, 1)
                    test_loss = criterion(outputs, labels)
                    total += labels.size(0)
                    correct += (predicted == labels).sum()

                print ("Test Accuracy : %.3f%%" % (100 * correct / total))
                acc = 100.* correct / total
                
                file1.write("Epoch=%03d,Accuracy= %.3f%%" % (epoch + 1, acc))
                file1.write(", Loss:%.3f" % (test_loss))
                file1.write("\n")
                file1.flush()
                
                if acc > best_acc :
                    if acc > 85 :
                        print ("Saving Model--->")
                        torch.save(net.state_dict(), 'RDPnetmodel'+str(epoch+1)+'.pth')
                    file3 = open("best_acc_RDPnet.txt","a")
                    file3.write ("Epoch=%d, best_acc=%.3f%%" % (epoch+1, acc))
                    file3.write ("\n")
                    file3.close()
                    best_acc = acc