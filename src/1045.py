# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:48:30 2017

@author: Matheus
"""

a,b,c = input().split()
a,b,c =[float(a),float(b),float(c)]
l = [a,b,c]
l.sort()
 
a = l[2]
b = l[1]
c = l[0]

if a>= (b+c):
    print ("NAO FORMA TRIANGULO")
else:    
    if ((a*a) == (b*b + c*c)):
        print ("TRIANGULO RETANGULO")
    if ((a*a) > (b*b + c*c)):
        print ("TRIANGULO OBTUSANGULO")
    if ((a*a) < (b*b + c*c)):
        print ("TRIANGULO ACUTANGULO")
    if ((a==b) and (b==c)):
        print ("TRIANGULO EQUILATERO")
    elif (b==c) or (a==b) or (a==c):
        print ("TRIANGULO ISOSCELES")
     