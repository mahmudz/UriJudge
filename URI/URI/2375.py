n = int(input())
a,b,c = (int(i) for i in input().split())
if(n <= a and n<=b and n<=c):
	print("S")
else:
	print("N")