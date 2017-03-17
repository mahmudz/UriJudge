# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 17:15:50 2017

@author: Matheus
"""


def winner(x,y):
    if(x=='tesoura'):
        if(y=='papel' or y=='lagarto'):
            return 1
        elif(y=='Spock' or y=='pedra'):
            return 0
    elif(x=='papel'):
        if(y=='pedra' or y=='Spock'):
            return 1
        elif(y=='lagarto' or y=='tesoura'):
            return 0
    elif(x=='pedra'):
        if(y=='lagarto' or y=='tesoura'):
            return 1
        elif(y=='papel' or y=='Spock'):
            return 0
    elif(x=='lagarto'):
        if(y=='Spock' or y=='papel'):
            return 1
        elif(y=='tesoura' or y=='pedra'):
            return 0
    elif(x=='Spock'):
        if(y=='tesoura' or y=='pedra'):
            return 1
        elif(y=='papel' or y=='lagarto'):
            return 0
            
         
    

n = int(input())

for i in range(n):
    sheldon,raj = input().split()
    if(sheldon != raj):
        if(winner(sheldon,raj)==1):
            print ("Caso #%d: Bazinga!"%(i+1))
        else:
            print ("Caso #%d: Raj trapaceou!"%(i+1))
    else:
        print ("Caso #%d: De novo!"%(i+1))