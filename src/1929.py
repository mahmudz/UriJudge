# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:28:17 2017

@author: Matheus
"""
def func(a,b,c):
    if((a+b)>c and(b+c)>a and (a+c)>b):
        return True
    return False

L = input().split()
L= [int(i) for i in L]
L.sort()

if(func(L[0],L[1],L[2])==True):
    print ("S")
elif(func(L[1],L[2],L[3])==True):
    print ("S")
elif(func(L[0],L[2],L[3])==True):
    print ("S")
elif(func(L[0],L[1],L[3])==True):
    print ("S")
else:
    print("N")


