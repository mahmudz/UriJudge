# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 19:28:20 2017

@author: Matheus
"""

a = [int(z) for z in input().split()]
b = [int(x) for x in input().split()]

if(a[0]+b[0]==1 and a[1]+b[1]==1 and a[2]+b[2]==1 and a[3]+b[3]==1 and a[4]+b[4]==1):
    print("Y")
else:
    print("N")
