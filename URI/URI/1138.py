import string


#brute force = time out :-(
numbers = string.digits
while True:
	dic = dict.fromkeys(numbers,0)
	i,f = (int(i) for i in input().split())
	if(i==0 and f==0):
		break
	for k in range(i,f+1):
		x = str(k)
		for ch in x:
			dic[ch] +=1

	resp = " ".join(str(s) for s in dic.values())
	print(resp)
