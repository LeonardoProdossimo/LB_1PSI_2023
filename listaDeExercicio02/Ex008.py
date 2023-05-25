#8- Faça um algoritmo que receba a idade de 75 pessoas e mostre mensagem informando “maior de idade” e “menor de idade” para cada pessoa. Considere a idade a partir de 18 anos como maior de idade.

import random

id = random.randint(0, 100)

for i in range(75):
    id = random.randint(0, 100)
    if(id<18):
        print(f"Sua idade é {id} e você não está na maioridade!")
        print('-'*40)
    else:
        print(f'Sua idade é {id} e você está na maioridade!')
        print('-'*40)
    i=i+1
print(f'O programa leu um total de {i} idades diferentes!')