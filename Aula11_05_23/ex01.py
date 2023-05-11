n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = 0
if n1 > n2:
    for i in range(n1,n2+1):
        if i%2==0:
            soma=soma+i
else:
    for i in range(n2,n1+1):
        if i%2==0:
            soma=soma+i
print (soma)
