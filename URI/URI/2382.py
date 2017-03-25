import math

a,b,c,d = (int(i) for i in input().split())
diagonal = math.sqrt(a*a + b*b + c*c)
if(2*d >=diagonal):
	print("S")
else:
	print("N")