v = []
for i in range(4):
	z = [(i) for i in input()]
	v.append(z)
f = int("".join( (v[i][0] for i in range(4))))
l = int("".join( (v[i][len(z)-1] for i in range(4))))

resp =""
for x in range(1,len(z)-1):
	tmp = int("".join( (v[i][x] for i in range(4))))
	c = f*tmp + l
	resp += chr(c%257)

print(resp)

