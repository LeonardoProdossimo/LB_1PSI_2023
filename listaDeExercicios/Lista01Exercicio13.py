#Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.

preco = float(input('Digite o custo do produto: '))
percentual = float(input('Digite o percentual de acréscimo no produto: '))
per = percentual / 100
total = preco * per + preco
print(f'O preço total do produto é R$ {total:.2f}')