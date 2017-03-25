# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 02:27:40 2017

@author: Matheus
"""

n = int(input())

if n ==1:
    print ("Ho!")
else:
    print("Ho",end="")
    for x in range(1,n):
        print (" Ho",end="")
    print ("!")