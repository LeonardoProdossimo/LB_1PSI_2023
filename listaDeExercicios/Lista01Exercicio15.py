#Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos dias de vida ela possui. Considere sempre anos completos, e que um ano possui 365 dias. Ex: uma pessoa com 19 anos possui 6935 dias de vida; veja um exemplo de saída:
#Ex: Tibúrcio, você já viveu 6935 dias.

nome = input('Digite seu nome: ')
id = int(input('Digite quantos anos você tem: '))
dias = id * 365
print(f'Olá {nome}, você já viveu {dias} dias.')