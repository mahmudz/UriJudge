# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 22:21:06 2017

@author: Matheus
"""

p,n = input().split()
p,n=int(p),int(n)
L = [int(i) for i in input().split()]
perdeu = False
for i in range(n-1):
    dif = abs(L[i]-L[i+1])
    if(dif > p):
        perdeu = True
        print("GAME OVER")
        break
if(perdeu == False):
    print("YOU WIN")