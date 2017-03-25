n = int(input())
s = [int(i) for i in input().split()]
maior = -9999
maior_count = -9999
for i in s:
	if(s.count(i)>maior_count):
		maior_count = s.count(i)
		maior = i
	elif(s.count(i)==maior_count):
		if(i > maior):
			maior = i
print(maior)