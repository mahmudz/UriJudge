# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 00:02:10 2017

@author: Matheus
"""

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    v = "ABCDEFGHIJKLMNOPQRSTUV"
    k=0
    while n:
        if(n<1):
            break
        a = int(n%b)
        if(a<10):
            digits.append(a)
        else:
            digits.append(v[a-10])
        n /= b
        k+=1
    return digits[::-1]

while True:
    n = int(input())
    if(n==0):
        print(0)
        break
    s = numberToBase(n,32)
    x = ''.join(str(e) for e in s)
    print(x)