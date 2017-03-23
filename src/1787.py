import math

def ehpotencia(x):
    x = math.log2(x)
    if(x==math.ceil(x)):
        return True
    return False

while True:
    n = int(input())
    if(n==0):
        break
    u =0
    r = 0
    g =0
    for i in range(n):
        a,b,c = map(int,input().split())
        print("Uri")
        if(ehpotencia(a)):
            u+=1
            if (a > b and a > c):
                u += 1
        if(ehpotencia(b)):
            r+=1
            if (b > a and b > c):
                r += 1
        if(ehpotencia(c)):
            g+=1
            if (c > a and c > b):
                g += 1
    v = [u,r,g]
    v.sort()
    v.reverse()
    if(v[0]==v[1] and v[0]==v[2]):
        print("URI")
    elif(v[0] == v[1]):
        print("URI")
    elif(v[0]==u):
        print("Uilton")
    elif(v[0]==r):
        print("Rita")
    elif(v[0]==g):
        print("Ingred")