n = int(input())
palavras = [str(s) for s in input().split()]
resp =""
k=0
for palavra in palavras:
	if(len(palavra)!=3):
		if(k==0):
			resp+=palavra
		else:
			resp= resp + " " + palavra
	else:
		if(palavra[0]=='O' and palavra[1]=='B'):
			if(k==0):
				resp+="OBI"
			else:
				resp+=" OBI"
		elif(palavra[0]=='U' and palavra[1]=='R'):
			if(k==0):
				resp+="URI"
			else:
				resp+=" URI"
		else:
			if(k==0):
				resp+=palavra
			else:
				resp = resp+ " " + palavra
	k+=1
print(resp)
