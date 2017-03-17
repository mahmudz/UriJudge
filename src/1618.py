# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:53:42 2017

@author: Matheus
"""

n = int(input())
for i in range(n):
    ax,ay,bx,by,cx,cy,dx,dy,rx,ry = [int(x) for x in input().split()]
    if(rx>=ax and rx<=bx and rx>=dx and rx<=cx and ry>=ay and ry<=dy and ry>=by and ry<=cy):
        print(1)
    else:
        print(0)
