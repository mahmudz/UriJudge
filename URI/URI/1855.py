# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 22:00:20 2017

@author: Matheus
"""

n = int(input()) #columns
m = int(input()) #rows
maximo = m*n
mapa = [['.' for i in range(m)]for j in range(n)]
for i in range(m):
    mapa[i] = [z for z in input()]
direction = mapa[0][0]
i = 0 #i = rows
j = 0 #j = columns
sair = False
k=0
while True:
    k+=1
    if(k>maximo):
        print("!")
        break
    if(mapa[i][j]=='*'):
        print("*")
        break
    if(mapa[i][j] != '.'):
        direction = mapa[i][j]
    if(direction == '>'):
        j+=1
    elif(direction == '<'):
        j-=1
    elif(direction == 'v'):
        i+=1
    elif(direction == '^'):
        i-=1
    if(i>=m or i<0 or j>=n or j<0):
        print("!")
        break


