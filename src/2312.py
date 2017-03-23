from operator import itemgetter, attrgetter, methodcaller
class Country:
	def __init__(self, name,gold,silver,bronze):
		self.name = name
		self.gold = gold
		self.silver = silver
		self.bronze = bronze
n = int(input())
v = []
while n!=0:
	n-=1
	c = [i for i in input().split()]
	v.append(Country(c[0],int(c[1]),int(c[2]),int(c[3])))

v = sorted(sorted(v,key=attrgetter('name'),reverse = True), key=attrgetter('gold','silver','bronze'))
v=v[::-1]
for i in range(len(v)):
	print(v[i].name,v[i].gold,v[i].silver,v[i].bronze)

