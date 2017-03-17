# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 23:39:54 2017

@author: Matheus
"""

def f(x,y):
    if(x=="pedra"):
        if(y=="pedra"):
            return("Sem ganhador")
        elif(y=="papel"):
            return("Jogador 1 venceu")
        elif(y=="ataque"):
            return ("Jogador 2 venceu")
    elif(x=="papel"):
        if(y=="pedra"):
            return("Jogador 2 venceu")
        elif(y=="papel"):
            return("Ambos venceram")
        elif(y=="ataque"):
            return ("Jogador 2 venceu")
    elif(x=="ataque"):
        if(y=="pedra"):
            return("Jogador 1 venceu")
        elif(y=="papel"):
            return("Jogador 1 venceu")
        elif(y=="ataque"):
            return ("Aniquilacao mutua")

n = int(input())
for i in range(n):
    a = input()
    b = input()
    print(f(a,b))