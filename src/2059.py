# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 16:32:47 2017

@author: Matheus
"""

p,j1,j2,r,a=input().split()
p,j1,j2,r,a = int(p),int(j1),int(j2),int(r),int(a)

if(p==1): #jogador 1 escolheu par
    if((j1+j2)%2==0):#total foi par
        if(r==1): #jogador 1 roubou
            if(a==1): #jogador 2 acusou roubo
                print("Jogador 2 ganha!")
            elif(a==0):#jogador 2 nao acusou roubo
                print("Jogador 1 ganha!")
        elif(r==0): #jogador 1 nao roubou
            if(a==1): #jogador 2 acusou roubo
                print("Jogador 1 ganha!")
            elif(a==0):#jogador 2 não acusou roubo
                print("Jogador 1 ganha!")
    else:#resultador foi impar
        if(r==1): #jogador 1 roubou
            if(a==1): #jogador 2 acusou roubo
                print("Jogador 2 ganha!")
            elif(a==0):#jogador 2 nao acusou roubo
                print("Jogador 1 ganha!")
        elif(r==0): #jogador 1 nao roubou
            if(a==1): #jogador 2 acusou roubo
                print("Jogador 1 ganha!")
            elif(a==0):#jogador 2 não acusou roubo
                print("Jogador 2 ganha!")
else:
    if((j1+j2)%2==0):#total foi par
        if(r==1): #jogador 1 roubou
            if(a==1): #jogador 2 acusou roubo
                print("Jogador 2 ganha!")
            elif(a==0):#jogador 2 nao acusou roubo
                print("Jogador 1 ganha!")
        elif(r==0): #jogador 1 nao roubou
            if(a==1): #jogador 2 acusou roubo
                print("Jogador 1 ganha!")
            elif(a==0):#jogador 2 não acusou roubo
                print("Jogador 2 ganha!")
    else:#resultador foi impar
        if(r==1): #jogador 1 roubou
            if(a==1): #jogador 2 acusou roubo
                print("Jogador 2 ganha!")
            elif(a==0):#jogador 2 nao acusou roubo
                print("Jogador 1 ganha!")
        elif(r==0): #jogador 1 nao roubou
            if(a==1): #jogador 2 acusou roubo
                print("Jogador 1 ganha!")
            elif(a==0):#jogador 2 não acusou roubo
                print("Jogador 1 ganha!")