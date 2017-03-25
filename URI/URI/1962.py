# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:43:10 2017

@author: Matheus
"""

n=int(input())
for i in range(n):
    a = int(input())
    resp = 2015-a
    if(resp<0):
        print ("%d A.C"%int(abs(resp)+1))
    elif (resp>0):
        print ("%d D.C"%resp)
    else:
        print ("1 A.C")
