import random
print('-'*50)
nSorte=int(input("Digite um número de 1 a 10: "))
while nSorte<0 or nSorte>10:
    print('Opção inválida tente novamente!')
    print('-'*35)
    nSorte=int(input(":Digite um número de 1 a 10: "))
print('-'*35)
print(f'Número da sorte é {nSorte}')
print('-'* 35)

randomicos = random.randint(0, 10)
soma=0
quant=1

while nSorte!=randomicos:
    randomicos = random.randint(0, 10)
    soma=soma+randomicos
    quant=quant + 1
    print('-'* 30)
    print(f'Números aleatório: {randomicos}')
print('-'* 50)
print(f'Foram gerados {quant} números aleatórios!')
print(f'A soma dos números aleatórios até chegar no seu número da sorte é {soma}')
print('-'* 80)


