# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 15:40:03 2017

@author: Matheus
"""

a,b=input().split()
a,b=int(a),int(b)
resp = (a+b)*(b-a+1)//2
print(resp)