# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 23:48:30 2017

@author: Matheus
"""

while True:
    try:
        pi = 3.14
        v = float(input())
        r = float(input())/2
        h = v/(pi*r*r)
        print("ALTURA = %.2f"%h)
        area = pi*r*r
        print("AREA = %.2f"%area)
    except:
        break

