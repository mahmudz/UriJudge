n, k = (int(i) for i in input().split())
v = []
for i in range(n):
	v.append(input())
print(sorted(v)[k-1])