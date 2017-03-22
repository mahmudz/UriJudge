from datetime import date
d0=date(2016,11,7)
while True:
	n = str(input())
	n = [int(i) for i in n.split(sep = "/")]
	d1 = date(n[2],n[1],n[0])
	delta = d0-d1
	delta  = delta.days
	s =""
	restof = delta%23 # 11-1-11 
	restoe = delta%28 # 14-14 #7P-7N-7P-7N
	restoi = delta%33 # 16-1-16 

	if(restof >0 and restof<11):
		s+="POSITIVO"
	elif(restof==11 or restof==0):
		s+="ZERADO"
	else:
		s+="NEGATIVO"

	s+= " "
	if(restoe >0 and restoe<14):
		s+="POSITIVO"
	elif(restoe==14 or restoe==0):
		s+="ZERADO"
	else:
		s+="NEGATIVO"
	s+= " "
	if(restoi >0 and restoi<=16):
		s+="POSITIVO"
	elif(restoi==17 or restoi==0):
		s+="ZERADO"
	else:
		s+="NEGATIVO"
	print(delta)
	print(s)