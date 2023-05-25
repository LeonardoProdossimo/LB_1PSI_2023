#9- Uma concessionária de veículos está vendendo os seus veículos com desconto. Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente de vários carros. O desconto deverá ser calculado de acordo com o ano do veículo. Até 2000 - 12% e acima de 2000 - 7%. O sistema deverá perguntar se deseja continuar calculando desconto até que a resposta seja: “(N) Não”. Informar total de carros com ano até 2000 e total geral.

print('-'*40)
p = input('Deseja consultar um veículo? Digite S pra Sim e N para não:: \n')

qtdAno = 0
qtdGeral = 0
while p.upper()!="S" and p.upper()!="N":
    print('-'*40)
    print('Resposta inválida, digite novamente!')
    p = input('Deseja consultar um veículo? Digite S pra Sim e N para não::  \n')

while p.upper()!="N":
    print('-'*40)
    modelo = input("Digite qual o modelo do carro: ")
    ano = int(input('Digite o ano do veículo: '))
    while ano < 1886:
        print('-'*40)
        print('Ano inválido, nem existiam automoveis neste ano! Digite novamente as informações: ')
        modelo = input("Digite qual o modelo do carro: ")
        ano = int(input('Digite o ano do veículo: '))
    valor = float(input("Digite o valor do carro: "))
    while valor < 0:
        print('-'*40)
        print('Valor inválido, digite novamente as informações! ')
        modelo = input("Digite qual o modelo do carro: ")
        ano = int(input('Digite o ano do veículo: '))
        valor = float(input("Digite o valor do carro: "))
    if ano <= 2000:
        nValor = valor-(valor*0.12)
        print('-'*40)
        print(f"O veiculo consultado custava R${valor:.2f} receberá 12% de desconto e custará R${nValor:.2f} ")
        qtdAno += 1
    if ano > 2000:
        nValor=valor-(valor*0.07)
        print('-'*40)
        print(f"O veiculo consultado custava R${valor:.2f} receberá 7% de desconto e custará R${nValor:.2f} ")

    qtdGeral +=1
    print('-'*40)
    p = input('Deseja consultar outro veículo? Digite S pra Sim e N para não:: \n')    
    while p.upper()!="S" and p.upper()!="N":
        print('-'*40)
        print('Resposta inválida, digite novamente!')
        p = input('Deseja consultar outro veículo? Digite S pra Sim e N para não::  \n')
    if p.upper()=="N":
        break
print('-'*40)
print(f'Foi consultado {qtdGeral} veiculos, sendo, {qtdAno} veiculos com ano até 2000.')