# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 00:48:40 2017

@author: Matheus
"""
import math
n = int(input())
a = ((1+math.sqrt(5))/2)**n
a -=  ((1-math.sqrt(5))/2)**n
a/=math.sqrt(5)
print("%.1f"%a)
