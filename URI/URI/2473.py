f = set([int(i) for i in input().split()])
s = set([int(i) for i in input().split()])
z = len(f.intersection(s))
if(z<3):
	print("azar")
elif(z==3):
	print("terno")
elif(z==4):
	print("quadra")
elif(z==5):
	print("quina")
elif(z==6):
	print("sena")
