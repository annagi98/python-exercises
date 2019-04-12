# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 23:17:29 2017

@author: Ania
"""

list=[]

import random

for i in range(100):
    list.append(random.randint(1,100))
    
print(list)


def bubbleSort(list):
    for index in range(len(list)-1,0,-1):
        for i in range(index):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp


bubbleSort(list)
print(list)