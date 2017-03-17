# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 17:28:39 2017

@author: Matheus
"""

a,b = [int(x) for x in input().split()]
t =1
while True:
    if((b*t-a*t)>=b):
        print(t)
        break
    t+=1