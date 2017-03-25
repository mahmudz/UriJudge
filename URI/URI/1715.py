# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 21:28:27 2017

@author: Matheus
"""
# n = numero de jogadores -> ROWS
# m = numero de partidas -> COLUMNS

n,m =[int(x) for x in input().split()]
mat = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    mat[i] = [int(x) for x in input().split()]
ver = [False for i in range(n)]
for i in range(n):
    for j in range(m):
        if(mat[i][j]==0):
            ver[i] = True
cont=0
for i in range(n):
    if(ver[i] == False):
        cont+=1
print(cont)

