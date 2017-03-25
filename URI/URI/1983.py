# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:38:21 2017

@author: Matheus
"""

n = int(input())
maior = -9999
resp = 0
for i in range(n):
    a,b = input().split()
    a,b =int(a),float(b)
    if(b>maior):
        maior = b
        resp = a
if(maior >=8):
    print(resp)
else:
    print("Minimum note not reached")
