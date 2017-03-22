c = input()
v = [i for i in input().split()]
quant =0
total =0
for i in v:
	quant+=1
	if(i.count(c)>=1):
		total+=1

resp = 100*total/quant
print("%.1f"%resp)