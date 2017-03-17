# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:00:10 2017

@author: Matheus
"""

r,c = input().split()
r,c=int(r),int(c)
m = [[0 for x in range(c)] for y in range(r)]
for i in range(r):
    L = [int(k) for k in input().split()]
    for j in range(c):
        m[i][j]=L[j]

entrou = False
for i in range(r):
    for j in range(c):
        if(m[i][j]==42):
            if(i-1>=0 and j-1>=0 and i+1 <r and j+1 <c):
                if(m[i-1][j]==7 and m[i+1][j]==7 and m[i-1][j-1]==7 and
                   m[i-1][j+1]==7 and m[i][j-1]==7 and m[i][j+1]==7 and m[i+1][j-1]==7 and m[i+1][j]==7 and m[i+1][j+1]==7):
                    entrou = True
                    print(i+1,j+1)

if(entrou == False):
    print("0","0")
