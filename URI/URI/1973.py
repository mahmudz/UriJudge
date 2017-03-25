# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 14:05:26 2017

@author: Matheus
"""
import re
n = int(input())

a = input()
a = re.findall(r'\d+',a)
a = [int(i) for i in a]

visitado = [0 for i in range(n)]
apontador = 0
while True:
    if(apontador <0 or apontador > n-1):
        break
    if(a[apontador]>0):
        a[apontador]-=1
        visitado[apontador]=1
        if((a[apontador]+1)%2==0):
            apontador -=1
        else:
            apontador+=1
    else:
        if((a[apontador])%2==0):
            apontador -=1
        else:
            apontador+=1
totalvisitado = sum(visitado)
final = sum(a)
print(totalvisitado,(final))


