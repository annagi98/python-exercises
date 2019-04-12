# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:37:16 2017

@author: Ania
"""



list=[]
import random
for i in range(50):
    list.append(random.randint(1,50))   
print(list)

list1=list.copy()
list2=list.copy()
list3=list.copy()
list4=list.copy()
list5=list.copy()
list6=list.copy()

#WYBIERANIE
def selectionSort(list1):
   for index in range(len(list1)-1,0,-1):
       index_najwiekszego=0
       for obecne_miejsce in range(1,index+1):
           if list1[obecne_miejsce]>list1[index_najwiekszego]:
               index_najwiekszego = obecne_miejsce

       list1[index],list1[index_najwiekszego]=list1[index_najwiekszego],list1[index]


selectionSort(list1)
print(list1)


#WSTAWIANIE
def insertionSort(list2):
   for index in range(1,len(list2)):

     obecna_wartosc = list2[index]
     obecne_miejsce = index

     while obecne_miejsce>0 and list2[obecne_miejsce-1]>obecna_wartosc:
         list2[obecne_miejsce]=list2[obecne_miejsce-1]
         obecne_miejsce = obecne_miejsce-1

     list2[obecne_miejsce]=obecna_wartosc


insertionSort(list2)
print(list2)


#BABELKOWE
def bubbleSort(list3):
    for index in range(len(list3)-1,0,-1):
        for i in range(index):
            zmiana=0
            if list3[i]>list3[i+1]:
                list3[i],list3[i+1]=list3[i+1],list3[i]
                zmiana=1
            if(zmiana==0):
                exit

bubbleSort(list3)
print(list3)


#QUICKSORT
def quickSort(list4):
   pomocnikQuicksorta(list4,0,len(list4)-1)
 
def pomocnikQuicksorta(list4,k,s):
   if k<s:
 
       punkt_podzialu = przegroda(list4,k,s)
 
       pomocnikQuicksorta(list4,k,punkt_podzialu-1)
       pomocnikQuicksorta(list4,punkt_podzialu+1,s)
 
 
def przegroda(list4,k,s):
   pivotvalue = list4[k]
 
   l_oznaczenie = k+1
   p_oznaczenie = s
 
   done = False
   while not done:
 
       while l_oznaczenie <= p_oznaczenie and list4[l_oznaczenie] <= pivotvalue:
           l_oznaczenie = l_oznaczenie + 1
 
       while list4[p_oznaczenie] >= pivotvalue and p_oznaczenie >= l_oznaczenie:
           p_oznaczenie = p_oznaczenie -1
 
       if p_oznaczenie < l_oznaczenie:
           done = True
       else:
           list4[l_oznaczenie],list4[p_oznaczenie]=list4[p_oznaczenie],list4[l_oznaczenie]
           
 
   list4[k],list4[p_oznaczenie]=list4[p_oznaczenie],list4[k]
   
 
   return p_oznaczenie
 
quickSort(list4)
print(list4)


#MERGESORT
def mergeSort(list5):
    if len(list5)>1:
        mid = len(list5)//2
        lewa_polowa = list5[:mid]
        prawa_polowa = list5[mid:]

        mergeSort(lewa_polowa)
        mergeSort(prawa_polowa)

        i=0
        j=0
        k=0
        while i < len(lewa_polowa) and j < len(prawa_polowa):
            if lewa_polowa[i] < prawa_polowa[j]:
                list5[k]=lewa_polowa[i]
                i=i+1
            else:
                list5[k]=prawa_polowa[j]
                j=j+1
            k=k+1

        while i < len(lewa_polowa):
            list5[k]=lewa_polowa[i]
            i=i+1
            k=k+1

        while j < len(prawa_polowa):
            list5[k]=prawa_polowa[j]
            j=j+1
            k=k+1

mergeSort(list5)
print(list5)


#KOPCOWANIE
def heapsort( list6 ):
    #zmienianie listy w kopiec
    dlugosc = len(list6)-1
    ostatni_rodzic = dlugosc // 2
    for i in range ( ostatni_rodzic, -1, -1 ):
        przesunWDol( list6, i, dlugosc )
 
    #zmienianie kopca w posortowana liste
    for i in range ( dlugosc, 0, -1 ):
        if list6[0] > list6[i]:
            swap( list6, 0, i )
            przesunWDol( list6, 0, i - 1 )
 
 
def przesunWDol( list6, pierwszy, ostatni ):
    najwiekszy = 2 * pierwszy + 1
    while najwiekszy <= ostatni:
        #prawe dziecko istnieje i jest wieksze od lewego dziecka
        if ( najwiekszy < ostatni ) and ( list6[najwiekszy] < list6[najwiekszy + 1] ):
            najwiekszy += 1
 
        #prawe dziecko jest wieksze od rodzica
        if list6[najwiekszy] > list6[pierwszy]:
            swap( list6, najwiekszy, pierwszy )
            #przesun w dol do pozycji najwiekszego dziecka
            pierwszy = najwiekszy;
            najwiekszy = 2 * pierwszy + 1
        else:
            return #wyjdz
 

def swap( A, x, y ):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp
 
heapsort(list6)
print(list6)

print(list)