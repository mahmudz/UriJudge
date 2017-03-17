# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 23:29:38 2017

@author: Matheus
"""

n = input()
n = int(n)
total=0.0
for i in range(n):
    a,b = input().split()
    a,b=int(a),int(b)
    if(a==1001):
        total+=(b*1.5)
    elif(a==1002):
        total+=(b*2.5)
    elif(a==1003):
        total+=(b*3.5)
    elif(a==1004):
        total+=(b*4.5)
    elif(a==1005):
        total+=(b*5.5)
print ("%.2f"%total)

