def fibo(n):
	if(n==1):
		return 0
	elif(n==2):
		return 1
	elif(n%2==0):
		return fibo(n-2)*fibo(n-1)
	else:
		return fibo(n-2)+fibo(n-1)
while True:
	try:
		n = int(input())
		print(fibo(n))
	except:
		break
