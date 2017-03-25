# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 12:02:06 2017

@author: Matheus
"""

n = int(input())
for i in range(n):
    j1,e1,j2,e2 = input().split()
    a,b = input().split()
    a,b = int(a),int(b)
    if((a+b)%2==0):
        if(e1== 'PAR'):
            print(j1)
        else:
            print(j2)
    else:
        if(e1=='IMPAR'):
            print (j1)
        else:
            print (j2)