# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 21:03:55 2017

@author: Matheus
"""

v = set()
for i in range(int(input())):
    s = input()
    v.add(s)
print("Falta(m) {} pomekon(s).".format((151-len(v))))