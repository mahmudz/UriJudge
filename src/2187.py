# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 00:08:35 2017

@author: Matheus
"""
k=0
while True:
    n = int(input())
    if(n==0):
        break
    k+=1
    notas = [50,10,5,1]
    v = [0]*4
    i=0
    while n!=0:
        if(notas[i] <= n):
            v[i]+=1
            n-=notas[i]
        else:
            i+=1
    print("Teste {}".format(k))
    print("{} {} {} {}".format(v[0],v[1],v[2],v[3]))
