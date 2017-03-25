# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 22:51:18 2017

@author: Matheus
"""

a,b = input().split()
a,b = int(a),int(b)

if(a==b):
    print (a)
else:
    if(a>b):
        print (a)
    else:
        print(b)