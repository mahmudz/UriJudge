# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 17:35:50 2017

@author: Matheus
"""

n = int(input())
for i in range(n):
    bonus = int(input())
    ad,dd,ld =input().split()
    ad,dd,ld =int(ad),int(dd),int(ld)
    ag,dg,lg =input().split()
    ag,dg,lg =int(ag),int(dg),int(lg)

    vd = (ad+dd)/2
    if(ld%2==0):
        vd+=bonus
    vg = (ag+dg)/2
    if(lg%2==0):
        vg+=bonus
    if(vg==vd):
        print("Empate")
    elif (vg>vd):
        print("Guarte")
    else:
        print("Dabriel")