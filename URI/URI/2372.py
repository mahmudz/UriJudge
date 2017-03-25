import math
a,b = (int(i) for i in input().split())
c,d = (int(i) for i in input().split())

resp = int(a*c + math.floor(a/b)*d)
print(resp)