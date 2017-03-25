k =0
while True:
	try:
		n,m = (float(i) for i in input().split())
		k+=1
		print("Projeto {}:".format(k))
		resp = (m/n -1)*100.00
		print("Percentual dos juros da aplicacao: {0:.2f} %\n".format(resp))
	except:
		break