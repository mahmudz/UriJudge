# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 17:46:10 2017

@author: Matheus
"""
while True:
    n = int(input())
    if(n==0):
        break
    else:
        for i in range(n):
            a = int(input())
            if(a%2==0):
                print(a*2-2)
            else:
                print(a*2-1)