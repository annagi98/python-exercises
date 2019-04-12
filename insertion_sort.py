# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 23:05:47 2017

@author: Ania
"""

list=[]

import random

for i in range(100):
    list.append(random.randint(1,100))
    
print(list)

def insertionSort(list):
   for index in range(1,len(list)):

     current_value = list[index]
     current_place = index

     while current_place>0 and list[current_place-1]>current_value:
         list[current_place]=list[current_place-1]
         current_place = current_place-1

     list[current_place]=current_value


insertionSort(list)
print(list)
