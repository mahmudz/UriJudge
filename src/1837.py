# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:58:28 2017

@author: Matheus
"""
import math
a,b= input().split()
a = int(a)
b = int(b)
if (b>0):
    q = math.floor(a/b)
elif (b<0):
    q = math.ceil(a/b)

r = a-b*q

print("%d %d"%(q,r))