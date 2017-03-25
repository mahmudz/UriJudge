# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 23:34:33 2017

@author: Matheus
"""

a,b = input().split()
a,b =int(a),int(b)
for i in range(b):
    n = input()
    if(n=="fechou"):
        a+=1
    elif(n=="clicou"):
        a-=1
print(a)