# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 21:37:50 2017

@author: Matheus
"""
import math
a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)

if a == 0.0:
    print ("Impossivel calcular")
else:
    s = b*b - 4*a*c
    if s <0:
        print ("Impossivel calcular")
    else:
        r1 = (-b+math.sqrt(s))/(2*a)
        r2 = (-b-math.sqrt(s))/(2*a)
        print ("R1 = %.5f"%r1)
        print ("R2 = %.5f"%r2)
                
                
            
        
        