#Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).

nome = input('Digite seu nome completo: ')
n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))
n3 = float(input('Digite o valor da terceira nota: '))
n4 = (n1+n2+n3)/3

print(f'Caro aluno {nome}, sua média é de {n4}.')