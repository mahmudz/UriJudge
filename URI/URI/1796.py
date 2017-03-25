# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 19:31:57 2017

@author: Matheus
"""

n = int(input())
a = [int(x) for x in input().split()]
s = sum(a)
media = s/n
if(media >= 0.5):
    print("N")
else:
    print("Y")