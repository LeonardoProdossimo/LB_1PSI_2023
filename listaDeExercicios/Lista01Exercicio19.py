#A lanchonete Gostosura vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias de queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de queijo ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, faça um algoritmo em que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as quantidades (em quilos) de queijo, presunto e carne necessários para compra

lanches = int(input('Digite a quantidade de lanches a serem feitos: '))

queijo = lanches * 0.10
presunto = lanches * 0.05
carne =  lanches * 0.10
print(f'Para fazer {lanches} lanches você vai precisar de {queijo} kg de queijo, {presunto} kg de presunto e {carne} kg de carne.')