n = int(input())
v = [i for i in input().split()]
p = int(input())
xs = [z for z in input().split()]

for x in xs:
	v.remove(x)

resp = " ".join(v)
print(resp)
