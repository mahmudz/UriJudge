# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:00:36 2017

@author: Matheus
"""

n = int(input())
resp=2
for i in range(n-1):
    resp = 1/resp
    resp+=2
resp = 1/resp
resp+=1
if(n==0):
    resp=1
print("%.10f"%resp)