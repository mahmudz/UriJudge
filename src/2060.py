# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 23:51:49 2017

@author: Matheus
"""

n =int(input())
L = input().split()
L = [int(i) for i in L]
dois = 0
tres = 0
quatro =0
cinco = 0
for i in range(n):
    if(L[i]%2==0):
        dois+=1
    if(L[i]%3==0):
        tres+=1
    if(L[i]%4==0):
        quatro+=1
    if(L[i]%5==0):
        cinco+=1
print ("%d Multiplo(s) de 2"%dois)
print ("%d Multiplo(s) de 3"%tres)
print ("%d Multiplo(s) de 4"%quatro)
print ("%d Multiplo(s) de 5"%cinco)

