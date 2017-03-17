# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:26:44 2017

@author: Matheus
"""

a = float(input())
if (a>0) and (a<=25):
    print ("Intervalo [0,25]")
elif (a>25) and (a<=50):
    print("Intervalo (25,50]")
elif (a>50) and (a<=75):
    print("Intervalo (50,75]")
elif (a>75) and (a<=100):
    print("Intervalo (75,100]")
    