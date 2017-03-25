# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:11:31 2017

@author: Matheus
"""

n = int(input())
resp=6
for i in range(n-1):
    resp = 1/resp
    resp+=6
resp = 1/resp
resp+=3
if(n==0):
    resp=3
print("%.10f"%resp)