while True:
    try:
        s = input()
        controle = 0
        for i in range(len(s)):
            if(i!=0):
                print(' '*(controle-1),end = ' ')
            for j in range(len(s)-controle):
                print(s[j],end = '')
                if(j!=len(s)-controle-1):
                    print(' ',end= '')
            controle+=1
            print()
        print()
    except:
        break
