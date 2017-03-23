p1,c1,p2,c2 = (float(i) for i in input().split())
if(p1*c1 == p2*c2):
	print("0")
elif(p1*c1 > p2*c2):
	print("-1")
else:
	print("1")