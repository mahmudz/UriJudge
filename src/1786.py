while True:
	try:
		x = input()
		x = [int(i) for i in x]
		total1=0
		total2=0
		k=9
		for i in range(len(x)):
			total1 += x[i]*(i+1)
			total2 += x[i]*(k)
			k-=1
		b1 = total1%11
		if(b1==10):
			b1 = 0
		b2 = total2%11
		if(b2==10):
			b2 = 0
		resp = str(x[0])+str(x[1])+str(x[2]) + "." + str(x[3])+str(x[4])+str(x[5]) + "." + str(x[6])+str(x[7])+str(x[8]) + "-" + str(b1) + str(b2)
		print(resp)
	except:
		break