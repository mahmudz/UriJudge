# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 01:59:01 2017

@author: Matheus
"""

while True:
    a,b = input().split()
    a,b=int(a),int(b)
    if(a==b and b==0):
        break
    resp = a+b
    resp = str(resp)
    f = ""
    for i in range(len(resp)):
        if(resp[i]!='0'):
            f+=resp[i]
    print(f)