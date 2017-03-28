#100% W.A, although the EXACTLY same implemetation works for C++ -.-

while True:
	try:
		n,m = (int(i) for i in input().strip().split())
		v = [int(c) for c in input().strip().split()]
		maior = max(v)
		z = [[] for i in range(maior+1)]
		d = dict(zip(range(1,maior+1),z))
		for i,c in enumerate(v):
			d[v[i]].append(i+1)
		for k in range(m):
			a,b = (int(i) for i in input().strip().split())
			if(len(d[b])<a):
				print("0")
			else:
				print("%d"%d[b][a-1])
	except:
		break

