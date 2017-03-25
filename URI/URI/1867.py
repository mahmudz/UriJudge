def ad(num):
	if(num==0):
		return 0
	if(num%9==0):
		return 9
	return num%9

while True:
	n,m = (int(i) for i in input().split())
	if(n==0 and m==0):
		break
	if(ad(n) > ad(m)):
		print(1)
	elif(ad(n) < ad(m)):
		print(2)
	else:
		print(0)