while True:
	try:
		n = int(input())
		d =[]
		for i in range(n):
			x = input()
			d.append(x)
		d = sorted(d)
		for i in d:
			print(i)
	except:
		break