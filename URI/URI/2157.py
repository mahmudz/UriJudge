n= int(input())
for i in range(n):
	x =""
	a,b = (int(i) for i in input().split())
	for i in range(a,b+1):
		x+=str(i)
	x = x + x[::-1]
	print(x)
