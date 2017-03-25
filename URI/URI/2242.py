# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 01:00:18 2017

@author: Matheus
"""

s = input()
x =""
for i in range(len(s)):
    if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
        x+=s[i]
rev = x[::-1]
if(x==rev):
    print("S")
else:
    print("N")