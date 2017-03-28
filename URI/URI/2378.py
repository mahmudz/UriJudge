n,c = (int(i) for i in input().split())
current = 0
excedeu = False
while n!=0:
    n-=1
    a,b = (int(i) for i in input().split())
    current -=a
    current+=b
    if(current>c):
        excedeu = True
if(excedeu):
    print("S")
else:
    print("N")