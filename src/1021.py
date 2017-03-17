# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 20:36:06 2017

@author: Matheus
"""
import math
n=float(input())
notas = int(n)
moedas = int(n*100-notas*100) 
print ("NOTAS:")
nt = int(notas/100)
print("%d nota(s) de R$ 100.00" % nt )
notas = (notas - nt*100)
nt = int(notas/50)
print("%d nota(s) de R$ 50.00" % nt )
notas = notas - nt*50
nt = int(notas/20)
print("%d nota(s) de R$ 20.00" % nt )
notas = notas - nt*20
nt = int(notas/10)
print("%d nota(s) de R$ 10.00" % nt )
notas = notas - nt*10
nt = int(notas/5)
print("%d nota(s) de R$ 5.00" % nt )
notas = notas - nt*5
nt = int(notas/2)
print("%d nota(s) de R$ 2.00" % nt )
notas = notas - nt*2
print ("MOEDAS:")
nt = int(notas/1)
print("%d moeda(s) de R$ 1.00" % nt )
mt = int(moedas/50)
print("%d moeda(s) de R$ 0.50" % mt )
moedas = moedas - mt*50
mt = int(moedas/25)
print("%d moeda(s) de R$ 0.25" % mt )
moedas = moedas - mt*25
mt = int(moedas/10)
print("%d moeda(s) de R$ 0.10" % mt )
moedas = moedas - mt*10
mt = int(moedas/5)
print("%d moeda(s) de R$ 0.05" % mt )
moedas = moedas - mt*5
mt = int(moedas/1)
print("%d moeda(s) de R$ 0.01" % mt )
moedas = moedas - mt*1
    

 

