n = int(input())
while n!=0:
	n-=1
	s = set()
	for i in range(int(input())):
		s.add(input())
	if(len(s)==1):
		print(next(iter(s)))
	else:
		print("ingles")
