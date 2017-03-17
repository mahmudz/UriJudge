# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 21:38:38 2017

@author: Matheus
"""
def f(p,x):
    if(x=="0"):
        return ""
    if(p==1):
        if(x=='1'):
            return "I"
        elif(x=='2'):
            return "II"
        elif(x=='3'):
            return "III"
        elif(x=='4'):
            return "IV"
        elif(x=='5'):
            return "V"
        elif(x=='6'):
            return "VI"
        elif(x=='7'):
            return "VII"
        elif(x=='8'):
            return "VIII"
        elif(x=='9'):
            return "IX"
    elif(p==2):
        if(x=='1'):
            return "X"
        elif(x=='2'):
            return "XX"
        elif(x=='3'):
            return "XXX"
        elif(x=='4'):
            return "XL"
        elif(x=='5'):
            return "L"
        elif(x=='6'):
            return "LX"
        elif(x=='7'):
            return "LXX"
        elif(x=='8'):
            return "LXXX"
        elif(x=='9'):
            return "XC"
    elif(p==3):
        if(x=='1'):
            return "C"
        elif(x=='2'):
            return "CC"
        elif(x=='3'):
            return "CCC"
        elif(x=='4'):
            return "ID"
        elif(x=='5'):
            return "D"
        elif(x=='6'):
            return "DC"
        elif(x=='7'):
            return "DCC"
        elif(x=='8'):
            return "DCCC"
        elif(x=='9'):
            return "CM"

n = input()
ni = int(n)
if(ni<10):
    resp =""
    resp+=f(1,n[0])
elif(ni>=10 and ni<100):
    resp= ""
    resp += f(2,n[0])
    resp += f(1,n[1])
elif(ni>=100 and ni<1000):
    resp= ""
    resp += f(3,n[0])
    resp += f(2,n[1])
    resp += f(1,n[2])
print(resp)