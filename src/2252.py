# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 20:15:59 2017

@author: Matheus
"""
k=0
while True:
    try:
        k+=1
        n = int(input())
        a = [float(x) for x in input().split()]
        b = a[:]
        b.sort()
        b.reverse()
        s=""
        #a é a lista original
        #b é a lista sortida em ordem reversa
        #procurar em a a posição de b[i]
        mm =0
        for i in range(n): #n é o tamanho da senha, logo imprimir os n maior numeros em a
            if(mm>=n):
                break
            for j in range(len(a)):
                if(b[i]==a[j]):
                    s+=str(j)
                    a[j]=-1
                    mm+=1
                if(mm>=n):
                    break
        print("Caso %d: %s"%(k,s))
    except:
        break