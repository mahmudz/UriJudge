# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 23:13:35 2017

@author: Matheus
"""

a,b,c = input().split()
a,b,c = int(a),int(b),int(c)

if(a > b) and (c>=b):
    print (":)")
elif (b > a) and (c <=b):
    print (":(")
elif (b > a) and (c > b) and ((c-b) < (b-a)):
    print (":(")
elif (b > a) and (c > b) and ((c-b) >= (b-a)):
    print(":)")
elif (a > b) and ( b >c) and ((b-c) < (a-b)):
    print(":)")
elif (a >b) and (b>c) and ((b-c) >= (a-b)):
    print(":(")
elif (a==b):
    if(c > b):
        print (":)")
    else:
        print (":(")