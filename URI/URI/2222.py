k = int(input())
for i in range(k):
    d ={}
    q = int(input())
    for j in range(q):
        v= input().split()
        d[str(j+1)] = [z for z in v[1:]]
    b = int(input())
    for m in range(b):
        h = [z for z in input().split()]
        print(0)
        if(h[0]=="1"):
#            l = [list(filter(set(d[h[1]]).__contains__,d[h[2]]))]
#            print(len(l))
            print(0)
        else:
#            l = set(d[h[1]]).union(d[h[2]])
            print(0)
#           print(len(l))
