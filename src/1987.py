while True:
	try:
		n,m = input().split()
		total =0
		for i in range(len(m)):
			total+=(int(m[i]))
		if(total%3==0):
			print(total,"sim")
		else:
			print(total,"nao")
	except:
		break