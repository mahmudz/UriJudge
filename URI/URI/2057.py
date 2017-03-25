# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 17:53:43 2017

@author: Matheus
"""

a,b,c = input().split()
a,b,c=int(a),int(b),int(c)
if(a+b+c<0):
    resp = 24-abs(a+b+c)
    print(resp)
elif(a+b+c<24):
    print(a+b+c)
elif(a+b>24):
    resp = abs(24-(a+b))
    resp +=c
    print(resp)

