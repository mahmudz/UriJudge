n = int(input())
if(n<=10):
	print(7)
elif(n>=11 and n<=30):
	resp = 7 + (n-10)*1
	print(resp)
elif(n>=31 and n<=100):
	resp = 7+ 20 + (n-30)*2
	print(resp)
elif(n>=101):
	resp = 7+20+140 +(n-100)*5
	print(resp)