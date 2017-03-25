def f(n):
    if(n<=1):
        return 1
    else:
        return n*f(n-1)

while True:
    try:
        n = input().strip()
        n = str(n)
        if(n=="0" or n==0 or n=='0'):
            break
        else:
            print(f(len(n)))
    except:
        break