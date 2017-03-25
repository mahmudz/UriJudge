while True:
    try:
        s = input()
        cor = True
        par =0
        closepar =0
        for i in s:
            if(i == '('):
                par +=1
            elif(i==')'):
                closepar+=1
            if(closepar > par):
                cor = False
        if(cor== True and par == closepar):
            print("correct")
        else:
            print("incorrect")
    except:
        break