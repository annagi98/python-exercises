# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 22:46:18 2017

@author: Ania
"""
#Sortowanie przez wybieranie

list=[]

import random

for i in range(100):
    list.append(random.randint(1,100))
    
print(list)


def selectionSort(list):
   for index in range(len(list)-1,0,-1):
       index_of_max=0
       for current_position in range(1,index+1):
           if list[current_position]>list[index_of_max]:
               index_of_max = current_position

       list[index],list[index_of_max]=list[index_of_max],list[index]


selectionSort(list)
print(list)


