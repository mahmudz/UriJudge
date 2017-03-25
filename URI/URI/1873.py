n = int(input())
while n!=0:
	n-=1
	a,b = (str(x) for x in input().split())
	if(a==b):
		print("empate")
	elif(a=="tesoura"):
		if(b=="papel" or b=="lagarto"):
			print("rajesh")
		elif(b=="spock" or b=="pedra"):
			print("sheldon")
	elif(a=="papel"):
		if(b=="pedra" or b=="spock"):
			print("rajesh")
		elif(b=="tesoura" or b=="lagarto"):
			print("sheldon")
	elif(a=="pedra"):
		if(b=="lagarto" or b=="tesoura"):
			print("rajesh")
		elif(b=="papel" or b=="spock"):
			print("sheldon")
	elif(a=="lagarto"):
		if(b=="spock" or b=="papel"):
			print("rajesh")
		elif(b=="pedra" or b=="tesoura"):
			print("sheldon")
	elif(a=="spock"):
		if(b=="tesoura" or b=="pedra"):
			print("rajesh")
		elif(b=="lagarto" or b=="papel"):
			print("sheldon")

