# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:49:54 2017

@author: Ania
"""

x=1.123456789*10e14
result1 = x + 0.1 - x
result2 = x - x + 0.1
print(result1)
print(result2)

#w pierwszym przypadku wynik to 0.125, a w drugim 0.1
#gdy za e liczba jest >14 to pierwszy wynik = 0.0
#gdy za e liczba = 14 to pierwszy wynik = 1.25
#gdy za e licxba jest <14 to pierwszy wynik <1.0 al wiekszy niz 0.0