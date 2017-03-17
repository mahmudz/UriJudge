# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 00:23:00 2017

@author: Matheus
"""
k=0
while True:
    n = int(input())
    if(n==0):
        break
    v = [int(x) for x in input().split()]
    k+=1
    print("Teste {}".format(k))
    for i in range(len(v)):
        if(v[i]-1 == i):
            print("{}\n".format(v[i]))