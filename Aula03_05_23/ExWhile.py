a=int(input("Digite o primeiro número: "))
b=int(input("Digite o segundo número: "))
c = 0
if a < b:
    while a<b:
        a+=1
        if a % 2 == 0:
            a+=1
            c+=1
    print(c)
elif a>b:
    while b < a:
        a-=1
        if b %2==0:
            a-=1
            c+=1
    print(c)
else:
    print("Fim")
    

    



    


    