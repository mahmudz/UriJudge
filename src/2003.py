# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 21:01:13 2017

@author: Matheus
"""
while True:
    try:
        a,b =input().split(':')
        a,b=int(a),int(b)
        minutos = a*60 + b + 60
        if(minutos > 8*60 ):
            print("Atraso maximo: %d"%int(minutos-8*60))
        else:
            print("Atraso maximo: 0")
    except:
        break

