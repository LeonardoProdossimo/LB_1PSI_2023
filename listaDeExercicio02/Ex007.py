#7- Ler 80 números e ao final informar quantos número(s) est(á)ão no intervalo entre 10 (inclusive) e 150 (inclusive).

import random

n = random.randint(0,1000)
q = 0
for i in range(81):
    if(n >= 10 and n <= 150):
        q = q + 1
    n = random.randint(0,1000)
    i=i+1
    print('-'*40)
    print(f'Número {n}')
print(f'O programa leu um total de {i} números e {q} estão dentro de 10(inclusive) e 150(inclusive)')