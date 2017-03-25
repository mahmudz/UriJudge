# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 16:55:21 2017

@author: Matheus
"""

def f(n):
    if(n==0):
        return 1
    else:
        return f(n-1)+n

k=0
while True:
    k+=1
    try:
        n =int(input())
        if(k!=1):
            print("\n")
        if(n==0):
            print("Caso %d : %d numero"%(k,f(n)))
        else:
            print("Caso %d : %d numeros"%(k,f(n)))
        print(0,end="")
        for i in range(n+1):
            for j in range(i):
                print (" %d"%i,end="")
    except:
        print("\n")
        break