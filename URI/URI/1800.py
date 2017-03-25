q,e = [int(i) for i in input().split()]
v = [int(i) for i in input().split()]
for i in range(q):
    n = int(input())
    if(n in v):
        print(0)
    else:
        print(1)
        v.append(n)