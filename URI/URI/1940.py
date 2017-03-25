j,r = (int(i) for i in input().split())
rodada = [0]*j
v = [int(i) for i in input().split()]
k=0
for i in range(len(v)):
	if(k>=j):
		k=0
	rodada[k]+=v[i]
	k+=1
maior = max(rodada)
resp =0
for i in range(j):
	if(maior == rodada[i]):
		resp = i
print(resp+1)