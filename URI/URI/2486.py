# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 13:49:11 2017

@author: Matheus
"""

def f(q,t):
    if(t=="suco"):
        return q*120
    elif(t=="morango"):
        return q*85
    elif(t=="mamao"):
        return q*85
    elif(t=="goiaba"):
        return q*70
    elif(t=="manga"):
        return q*56
    elif(t=="laranja"):
        return q*50
    elif(t=="brocolis"):
        return q*34
    return 0


while True:
    n = int(input())
    if(n==0):
        break
    total =0
    for i in range(n):
        x = [str(z) for z in input().split()]
        quant = int(x[0])
        tipo = str(x[1])
        total += f(quant,tipo)

    if(total>=110 and total<=130):
        print(total,"mg")
    elif(total<110):
        print("Mais",110-total,"mg")
    elif(total>130):
        print("Menos",total-130,"mg")
