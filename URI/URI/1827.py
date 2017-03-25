# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 17:42:35 2017

@author: Matheus
"""
while True:
    try:
        n=int(input())
        #matrix = [[0 for x in range(n)] for y in range(n)]
        matrix = [[0 for x in range(n)] for y in range(n)]
        interno = int(n/3)
        meio = int(n/2)
        for i in range(n):
            for j in range(n):
                if (i==0 or j==0):
                    matrix[i][j] = 0
                if(i==j):
                    matrix[i][j] = 2
                if((i+j)==(n-1)):
                    matrix[i][j] = 3
                if( i>= interno and i<= (n-interno-1) and j>=interno and j<= (n-interno-1) ):
                    matrix[i][j] = 1
                if(i==meio and j==meio):
                    matrix[i][j]=4
        for i in range(n):
            for j in range(n):
                print (matrix[i][j],end="")
            print ("")
        print ("")
    except:
        break