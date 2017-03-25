# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:28:31 2017

@author: Matheus
"""

a = list()

for x in range(100):
    tmp = float(input())
    a.append(tmp)

for x in range(100):
    if a[x]<=10:
        print ("A[%d] = %.1f" % (x, a[x]))