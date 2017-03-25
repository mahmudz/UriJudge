# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 02:02:10 2017

@author: Matheus
"""

n = int(input())
for i in range(n):
    a,b,c=input().split()
    a,b,c=int(a),int(b),int(c)
    sa = str(a)
    sb = str(b)
    if(a>=0 and a<10):
        sa = "0" + str(a)
    if(b>=0 and b<10):
        sb = "0" + str(b)
    if(c==1):
        print(sa+":"+sb+" - A porta abriu!")
    else:
        print(sa+":"+sb+" - A porta fechou!")
