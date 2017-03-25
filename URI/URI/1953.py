while True:
	try:
		n = int(input())
		epr =0
		ehd =0
		intruso =0
		for i in range(n):
			a,b = (i for i in input().split())
			if b=="EPR":
				epr+=1
			elif b=="EHD":
				ehd +=1
			else:
				intruso+=1
		print("EPR:",epr)
		print("EHD:",ehd)
		print("INTRUSOS:",intruso)
	except:
		break