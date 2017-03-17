# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 19:36:58 2017

@author: Matheus
"""

n = int(input())
la,lb = input().split()
la,lb = int(la),int(lb)
sa,sb = input().split()
sa,sb = int(sa),int(sb)

if(n>=la and n<=lb and n>=sa and n<=sb):
    print("possivel")
else:
    print("impossivel")