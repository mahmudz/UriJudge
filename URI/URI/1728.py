while True:
	try:

		s = input()
		a,b = s.split("+")
		b,c = b.split("=")
		a= int(a[::-1])
		b= int(b[::-1])
		c = int(c[::-1])
		if(a+b==c):
			print(True)
		else:
			print(False)
		if(a==0 and b==0 and c==0):
			break
	except:
		break