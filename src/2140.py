# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 01:07:05 2017

@author: Matheus
"""

while True:
    a,b =input().split()
    a,b=int(a),int(b)
    if(a==b and b==0):
        break
    troco = b-a
    if (troco == 4
        or troco == 10
        or troco == 20
        or troco == 40
        or troco == 100
        or troco == 200
        or troco == 7
        or troco == 12
        or troco == 22
        or troco == 52
        or troco == 102
        or troco == 15
        or troco == 25
        or troco == 55
        or troco == 105
        or troco == 30
        or troco == 60
        or troco == 110
        or troco == 70
        or troco == 120
        or troco == 150):
        print("possible")
    else:
        print("impossible")