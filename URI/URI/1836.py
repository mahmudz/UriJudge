import math
t = int(input())
k=0
for z in range(t):
	k+=1
	x = input().split()
	nome = x[0]
	lvl = int(x[1])
	print("Caso #{}: {} nivel {}".format(k,nome,lvl))
	bs,iv,ev = (int(i) for i in input().split())
	hp = ((iv+bs+((math.sqrt(ev))/8)+50)*lvl)/50+10
	hp= int(hp)
	print("HP: {}".format(hp))
	bs,iv,ev = (int(i) for i in input().split())
	s=((iv+bs+(math.sqrt(ev))/8)*lvl)/50 + 5
	s = int(s)
	print("AT: {}".format(s))
	
	bs,iv,ev = (int(i) for i in input().split())
	s=((iv+bs+(math.sqrt(ev))/8)*lvl)/50 + 5
	s = int(s)
	print("DF: {}".format(s))

	bs,iv,ev = (int(i) for i in input().split())
	s=((iv+bs+(math.sqrt(ev))/8)*lvl)/50 + 5
	s = int(s)
	print("SP: {}".format(s))
