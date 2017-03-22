c = input()
total =0
n = 0
k=0
while True:
	if(k>=len(c)):
		break
	tmp = c[k]
	if(tmp!='1'):
		n+=1
		total+=int(tmp)
	elif((k+1)<len(c)):
		if(c[k+1]=='0'):
			total+=10
			n+=1
			k+=1
		else:
			n+=1
			total+=1
	else:
		n+=1
		total+=1
	k+=1
print("%.2f"%(total/n))
