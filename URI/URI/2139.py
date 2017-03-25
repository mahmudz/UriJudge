# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:48:21 2017

@author: Matheus
"""
from datetime import date

while True:
    try:
        m,d=input().split()
        m,d=int(m),int(d)
        if(m==12 and d==24):
            print("E vespera de natal!")
        elif(m==12 and d==25):
            print("E natal!")
        elif(m==12 and d>25):
            print("Ja passou!")
        else:
            d0 = date(2016,m,d)
            dnatal = date(2016,12,25)
            delta = dnatal-d0
            print("Faltam " + str(delta.days) + " dias para o natal!")
    except:
        break