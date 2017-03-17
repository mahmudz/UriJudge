# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 00:22:30 2017

@author: Matheus
"""

n = int(input())
total_saque = 0
total_bloqueio = 0
total_ataques =0

stotal_saque = 0
stotal_bloqueio = 0
stotal_ataques =0

for i in range(n):
    nome = input()
    s,b,a = input().split()
    s,b,a = int(s),int(b),int(a)
    ss,bs,sa = input().split()
    ss,bs,sa = int(ss),int(bs),int(sa)
    total_saque+=s
    total_bloqueio+=b
    total_ataques+=a
    stotal_saque+=ss
    stotal_bloqueio+=bs
    stotal_ataques+=sa
ps = (stotal_saque/total_saque)*100
bs = (stotal_bloqueio/total_bloqueio)*100
ass = (stotal_ataques/total_ataques)*100
print("Pontos de Saque: %.2f"%ps + " %.")
print("Pontos de Bloqueio: %.2f"%bs + " %.")
print("Pontos de Ataque: %.2f"%ass + " %.")




