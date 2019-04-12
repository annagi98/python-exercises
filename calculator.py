# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 15:58:44 2017

@author: Ania
"""

#calculator

def adding(no_1, no_2):
    return no_1+no_2

def substracting(no_1, no_2):
    return no_1-no_2

def multiplying(no_1, no_2):
    return no_1*no_2

def dividing(no_1, no_2):
    return no_1/no_2

def exponentiation(no_1, no_2):
    return no_1**no_2

def main():
    type_of_action = int(input("What action do you want to perform? 1-adding 2-substracting 3-multiplying, 4-dividing, 5-exponentiation \n"))

    no_1 = int(input("Insert first number: "))
    no_2 = int(input("Insert second number: "))
    if(type_of_action==1):
        result=adding(no_1, no_2)
    if(type_of_action==2):
        result=substracting(no_1, no_2)
    if(type_of_action==3):
        result=multiplying(no_1, no_2)
    if(type_of_action==4):
        result=dividing(no_1, no_2)
    if(type_of_action==5):
        result=exponentiation(no_1, no_2)
        
    print("\nResult is: ")
    print(result)

    
main()