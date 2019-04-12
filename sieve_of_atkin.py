# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:09:06 2017

@author: Ania
"""

#writing out prime numbers up to a certain number
import math
is_prime = list()
limit = int(input("Write out prime numbers up to a number: "))
import time
start_time = time.time()
is_prime = [False] * (limit + 1)
for x in range(1,int(math.sqrt(limit))+1):
    for y in range(1,int(math.sqrt(limit))+1):
        n = 4*x**2 + y**2
        if n<=limit and (n%12==1 or n%12==5):
            is_prime[n] = not is_prime[n]            
        n = 3*x**2+y**2        
        if n<= limit and n%12==7:            
            is_prime[n] = not is_prime[n]            
        n = 3*x**2 - y**2        
        if x>y and n<=limit and n%12==11:            
            is_prime[n] = not is_prime[n]

for n in range(5,int(math.sqrt(limit))):
    if is_prime[n]:
        for k in range(n**2,limit+1,n**2):
            is_prime[k] = False
print ("2")
print ("3")
for n in range(5,limit):
    if is_prime[n]: print (n)
print("--- %s seconds ---" % (time.time() - start_time))
