# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:28:24 2017

@author: Ania
"""

list=[]
 
import random
 
for i in range(100):
    list.append(random.randint(1,100))
   
print(list)
 
 
def quickSort(list):
   helper(list,0,len(list)-1)
 
def helper(list,k,s):
   if k<s:
 
       pivot = partition(list,k,s)
 
       helper(list,k,pivot-1)
       helper(list,pivot+1,s)
 
 
def partition(list,k,s):
   pivotvalue = list[k]
 
   left_mark = k+1
   right_mark = s
 
   done = False
   while not done:
 
       while left_mark <= right_mark and list[left_mark] <= pivotvalue:
           left_mark = left_mark + 1
 
       while list[right_mark] >= pivotvalue and right_mark >= left_mark:
           right_mark = right_mark -1
 
       if right_mark < left_mark:
           done = True
       else:
           list[left_mark],list[right_mark]=list[right_mark],list[left_mark]
           
 
   list[k],list[right_mark]=list[right_mark],list[k]
   
 
   return right_mark
 
quickSort(list)
print(list)
 