# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 23:48:18 2017

@author: Matheus
"""
r=0
while True:
    try:
        s = input()
        if(s!='caw caw'):
            if(s[0]=='*'):
                r+=4
            if(s[1]=='*'):
                r+=2
            if(s[2]=='*'):
                r+=1
        else:
            print (r)
            r=0
    except:
        break