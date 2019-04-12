# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:15:40 2017

@author: Ania
"""

list=[]

import random

for i in range(100):
    list.append(random.randint(1,100))
    
print(list)

def mergeSort(list):
    if len(list)>1:
        mid = len(list)//2
        left_half = list[:mid]
        right_half = list[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i=0
        j=0
        k=0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list[k]=left_half[i]
                i=i+1
            else:
                list[k]=right_half[j]
                j=j+1
            k=k+1

        while i < len(left_half):
            list[k]=left_half[i]
            i=i+1
            k=k+1

        while j < len(right_half):
            list[k]=right_half[j]
            j=j+1
            k=k+1

mergeSort(list)
print(list)
