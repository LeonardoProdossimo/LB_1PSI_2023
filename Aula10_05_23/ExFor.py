import random

n = int(input("Digite a quantidade de vezes que será sorteado os números: "))
nSorte = nSorte=int(input("Digite um número de 1 a 10: "))
while nSorte<0 or nSorte>10:
    print('Opção inválida tente novamente!')
    print('-'*35)
    nSorte=int(input(":Digite um número de 1 a 10: "))
print('-'*35)
print(f'Número da sorte é {nSorte}')
print('-'* 35)
randomicos = random.randint(0, 10)
soma=0
for  i in range(n):
    randomicos = random.randint(0, 10)
    soma=soma+randomicos
    print('-'* 30)
    print(f'Números aleatório: {randomicos}')
print('-'* 50)
print(f'Foram gerados {n} números aleatórios!')
print(f'A soma dos números aleatórios até chegar no seu número da sorte é {soma}')
print('-'* 80)

