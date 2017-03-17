# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 19:52:53 2017

@author: Matheus
"""

while True:
    try:
        x,m = input().split()
        x,m =int(x),int(m)
        if(x+m==0):
            break
        print (int(x*m))
    except:
        break