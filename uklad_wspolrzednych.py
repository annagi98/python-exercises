# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 13:03:04 2017

@author: Ania
"""

print("Program wskazuje, w ktorej cwiartce ukladu wspolrzednych znajduje sie punkt.")
x=int(input("Podaj pierwsza wspolrzedna: "))
y=int(input("Podaj druga wspolrzedna: "))

if(x>0 and y>0):
    print("Punkt lezy w I cwiartce ukladu wspolrzednych")
    
if(x>0 and y<0):
    print("Punkt lezy w II cwiartce ukladu wspolrzednych")
    
if(x<0 and y<0):
    print("Punkt lezy w III cwiartce ukladu wspolrzednych")

if(x<0 and y>0):
    print("Punkt lezy w IV cwiartce ukladu wspolrzednych")

if(x==0):
    print("Punkt lezy na osi OY")

if(y==0):
    print("Punkt lezy na osi OX")
