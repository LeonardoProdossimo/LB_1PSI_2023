#5- Faça um programa que calcule e mostre a média aritmética de N notas. N equivale ao total de avaliações. 
print('-'*40)
n = int(input("Digite o número de notas que vc vai inserir: "))

while n < 0:
    print('-'*40)
    print('Número inválido, digite novamente!')
    n = int(input("Digite o número de notas que vc vai inserir: "))
media = 0
for i in range(n):
    nota = float(input("Digite a nota: "))
    nota = nota + media
    media = nota
print('-'*40)
print(f'Sua média é {media/n}')
    

