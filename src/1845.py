# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 18:17:32 2017

@author: Matheus
"""

lines = input()
resp = []
ult = False
for x in lines:
    if(x=='F' or x=='f' ):
        if(ult== False):
            resp.append(x)
            ult = True
    elif(x=='j' or x=='s' or  x=='p' or x=='v' or x=='b' or x=='x' or x=='z'):
        if(ult == False):
            resp.append('f')
            ult = True
    elif(x=='J' or x=='S' or  x=='P' or x=='V' or x=='B' or x=='X'or x=='Z'):
        if(ult == False):
            resp.append('F')
            ult = True
    else:
        ult = False
        resp.append(x)


imp = "".join(z for z in resp)
print(imp)
