v = [int(i) for i in input().split()]

if(v[0]<v[1] and v[1]<v[2] and v[2]<v[3] and v[3]<v[4]):
	print("C")
elif(v[0]>v[1] and v[1]>v[2] and v[2]>v[3] and v[3]>v[4]):
	print("D")
else:
	print("N")