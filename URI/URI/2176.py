# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:41:50 2017

@author: Matheus
"""

s = input()
total=0
for i in range(len(s)):
    if(s[i]=='1'):
        total+=1
if(total%2==0):
    s+="0"
else:
    s+="1"
print(s)