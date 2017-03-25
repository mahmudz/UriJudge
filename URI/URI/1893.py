# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 19:44:23 2017

@author: Matheus
"""

a,b=input().split()
a,b=int(a),int(b)

if(b>=a):
    if(b>=0 and b<=2):
        print("nova")
    elif(b>=3 and b<=96):
        print("crescente")
    elif(b>=97 and b<=100):
        print("cheia")
else:
    if(b>=3 and b<=96):
        print("minguante")
    elif(b>=0 and b<=2):
        print("nova")
    elif(b>=97 and b<=100):
        print("cheia")