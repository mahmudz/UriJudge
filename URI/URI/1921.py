# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 21:27:48 2017

@author: Matheus
"""
def f(n):
    if(n==4):
        return 2
    else:
        return f(n-1)+(n-2)

n = int(input())
resp=2
k = 3
if(n>3):
    for i in range(4,n):
        resp = resp+k
        k+=1
    print(resp)
else:
    print(0)