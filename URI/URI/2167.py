# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 21:56:16 2017

@author: Matheus
"""

n= int(input())
L = [int(i) for i in input().split()]
resp=0
for i in range(n-1):
    if(L[i] > L[i+1] and resp ==0):
        resp = i+1+1
print(resp)
