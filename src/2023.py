d = []
while True:
    try:
        x = str(input())
        d.append(x)
    except:
        break
d.sort(key=str.lower)
print(d[-1])


