# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 15:58:09 2017

@author: Matheus
"""

n = int(input())
for z in range(n):
    nome= input()
    grau = float(input())
    l = input().split()
    l = [float(i) for i in l]
    l.sort()
    del l[0]
    del l[len(l)-1]
    s = sum(l)
    resp = s*grau
    print ("%s %.2f"%(nome,resp))