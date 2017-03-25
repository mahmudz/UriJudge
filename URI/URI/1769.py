while True:
    try:
        cpf = str(input())
        cpf = cpf.replace(".","")
        t1 =0
        t2 =0
        k=9
        for i in range(0,9):
            t1 += (int(cpf[i]) * (i+1))
            t2 += (int(cpf[i]) *k)
            k-=1
        b1 = t1%11
        b2 = t2%11
        if(b1==10):
            b1=0
        if(b2==10):
            b2=0
        if(b1 == int(cpf[10]) and b2==int(cpf[11])):
            print("CPF valido")
        else:
            print("CPF invalido")
    except:
        break
