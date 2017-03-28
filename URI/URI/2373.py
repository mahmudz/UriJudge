n = int(input())
total =0
while n!=0:
    n-=1
    a,b = (int(i) for i in input().split())
    if(a>b):
        total+=b
print(total)

