# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 18:24:51 2017

@author: Matheus
"""

n = int(input())
a = [int(i) for i in input().split()]
if(n!=2):
    anterior = a[0]
    falhou = False
    for i in range(1,n-1):
        if(anterior > a[i]):
            if(a[i] >= a[i+1]):
                falhou = True
                print("0")
                break
        elif(anterior <a[i]):
            if(a[i] <=a[i+1]):
                falhou = True
                print("0")
                break
        anterior = a[i]
    if(falhou == False):
        print("1")
else:
    if(a[0]==a[1]):
        print("0")
    else:
        print("1")
