# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 12:16:30 2017

@author: Matheus
"""

a,b,c = input().split()
a,b,c = int(a),int(b),int(c)
entrou = False
if(a==b and b==c):
    print ("Valido-Equilatero")
    entrou = True
elif(a==b or b==c or a==c):
    print ("Valido-Isoceles")
    entrou = True
elif((a+b)>c and (a+c)>b and (b+c)>a):
    print ("Valido-Escaleno")
    entrou = True
if(entrou == True):
    if((a*a)==(b*b+c*c) or (b*b)==(a*a+c*c) or (c*c)==(a*a+b*b)):
        print ("Retangulo: S")
    else:
        print ("Retangulo: N")
else:
    print ("Invalido")