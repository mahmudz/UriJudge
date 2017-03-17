# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:57:37 2017

@author: Matheus
"""
import math
n = int(input())
minimo = n/math.log(n)
maximo = 1.25506*n/math.log(n)
print("%.1f %.1f"%(minimo,maximo))