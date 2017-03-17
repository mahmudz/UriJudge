# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:22:58 2017

@author: Matheus
"""

a,b = input().split()
a,b = [int(a),int(b)]


if a==1:
    resp = b*4.00
    print("Total: R$ %.2f"%resp)
elif a==2:
    resp = b*4.50
    print("Total: R$ %.2f"%resp)
elif a==3:
    resp = b*5.00
    print("Total: R$ %.2f"%resp)
elif a==4:
    resp = b*2.00
    print("Total: R$ %.2f"%resp)
elif a==5:
    resp = b*1.50
    print("Total: R$ %.2f"%resp)

