n = int(input("Digite um número: "))
numero = n
contador = 1
while n < 0:
    print('Número inválido, digite novamente!')
    n = int(input("Digite um número: "))
    while n//10!=0:
        n=n//10
        contador=contador+1
print(f'O número {numero} tem {contador} digitos')
    