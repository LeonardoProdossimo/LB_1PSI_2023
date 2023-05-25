#10 Faça um algoritmo que receba “N” números e mostre positivo, negativo ou zero para cada número

print('-'*40)
v = int(input("Digite o número de vezes que você irá brincar: "))

while v <= 0:
    print('-'*40)
    print('Número inválido, digite novamente!')
    v = int(input("Digite o número de notas que vc vai inserir: "))

x=0
y=0
z=0

for i in range(v):
    print('-'*40)
    n = float(input('Digite qualquer número: '))
    if n < 0:
        x+=1
        print('-'*40)
        print(f'O número {n} é negativo!')
    elif n == 0:
        y+=1
        print('-'*40)
        print(f'Esse é o número zero, {n}!')
    else:
        z+=1
        print('-'*40)
        print(f'O número {n} é positivo!')

print('-'*40)
print(f'Foi consultado {v} número(s), {x} número(s) negativo(s), {y} número(s) zero e {z} número(s) positivo(s)!')