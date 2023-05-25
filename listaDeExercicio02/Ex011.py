#11- Faça um algoritmo que receba o preço de custo e o preço de venda de 40 produtos. Mostre como resultado se houve lucro, prejuízo ou empate para cada produto. Informe a média de preço de custo e do preço de venda.

import random

custo1 = 0
venda1 = 0

for i in range(41):
    custo = random.randint(0,1000)
    custo+=custo1
    custo1 = custo

for j in range(41):
    venda =  random.randint(0,1000)
    venda+=venda1
    venda1 = venda

cal = (venda1 - custo1)
if cal > 0:
    print('-'*40)
    print(f'Você teve lucro de R${cal:.2f}')
elif cal == 0:
    print('-'*40)
    print(f'Você ficou empatado! ')
else:
    print('-'*40)
    print(f'Você teve prejuízo de R${cal*-1:.2f}')