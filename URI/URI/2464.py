d = {}
s = "abcdefghijklmnopqrstuvwxyz"
x =input().strip()

for c,i in enumerate(x): 
	d[i] = s[c]
resp =""

z =input().strip()
for c in z:
	resp += d[c]
print(resp)