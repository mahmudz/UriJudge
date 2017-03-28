na,da,va = (int(i) for i in input().split())
nb,db,vb = (int(i) for i in input().split())

ta = da/va
tb = db/vb

if(ta<tb):
    print(na)
else:
    print(nb)