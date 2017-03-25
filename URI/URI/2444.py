# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 23:56:55 2017

@author: Matheus
"""

v,t = [int(x) for x in input().split()]
z = [int(x) for x in input().split()]
for i in z:
    v +=i
    if(v<0):
        v =0
    elif(v>100):
        v=100
print(v)