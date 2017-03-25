# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 22:59:23 2017

@author: Matheus
"""

n = int(input())
a,b,c,d,e = input().split()
a,b,c,d,e = int(a),int(b),int(c),int(d),int(e)

cont = 0
if(a==n):
    cont+=1
if(b==n):
    cont+=1
if(c==n):
    cont+=1
if(d==n):
    cont+=1
if(e==n):
    cont+=1
print(cont)
