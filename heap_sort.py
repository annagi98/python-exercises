# -*- coding: utf-8 -*-
"""
Created on Wed Dec    6 23:21:03 2017

@author: Ania
"""
 
list=[]
 
import random
 
for i in range(100):
        list.append(random.randint(1,100))
     
print(list)
 
 
def heapsort( list ):
    #changing list to a heap
    length = len(list)-1
    last_rodzic = length // 2
    for i in range ( last_rodzic, -1, -1 ):
        move_down( list, i, length )
 
    #changing heap to a sorted list
    for i in range ( length, 0, -1 ):
        if list[0] > list[i]:
            swap( list, 0, i )
            move_down( list, 0, i - 1 )
 
 
def move_down( list, first, last ):
    largest = 2 * first + 1
    while largest <= last:
        #right child exists and is bigger than left child
        if ( largest < last ) and ( list[largest] < list[largest + 1] ):
            largest += 1
 
        #right child is bigger than parent
        if list[largest] > list[first]:
            swap( list, largest, first )
            #move down to the biggest child's position
            first = largest;
            largest = 2 * first + 1
        else:
            return 
 

def swap( A, x, y ):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp
 
heapsort(list)
print(list)