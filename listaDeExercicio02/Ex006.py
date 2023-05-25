#6- Escrever um algoritmo que lê o número de identificação, as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação. Calcular a média de aproveitamento, usando a fórmula:
# MA = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME )/7
# A atribuição de conceitos obedece a tabela abaixo:

# Média de Aproveitamento | Conceito
# MA >= 9,0               | A
# 7,5 <= MA < 9,0         | B
# 6,0 <= MA < 7,5         | C
# 4,0 <= MA < 6,0         | D
# MA < 4,0                | E

# O algoritmo deve escrever o suas notnúmero do aluno, as, a média dos exercícios, a média de aproveitamento, o conceito correspondente e a mensagem: APROVADO se o conceito for A, B ou C e REPROVADO se o conceito for D ou E. Pergunte se o usuário deseja digitar as notas de outro aluno S para sim e N para não
print('-'*40)
p = input('Deseja cadastrar um aluno? \n')

while p.upper()!="SIM" and p.upper()!="NÃO" and p.upper()!="NAO":
    print('-'*40)
    print('Resposta inválida, digite novamente!')
    p = input('Deseja cadastrar um aluno? \n')


while p.upper()!="NÃO" or p.upper()!="NAO":
    print('-'*40)
    id = int(input('Digite o número de identificação: '))

    while id < 0:
        print('-'*40)
        print('Número inválido, digite novamente!')
        id = int(input("Digite o número de identificação: "))
    print('-'*40)
    nota1 = float(input('Digite a primeira nota: '))

    while nota1 < 0:
        print('-'*40)
        print('Nota inválida, digite novamente!')
        nota1 = float(input("Digite a primeira nota: "))

    print('-'*40)
    nota2 = float(input('Digite a segunda nota: '))
    while nota1 < 0:
        print('-'*40)
        print('Nota inválida, digite novamente!')
        nota2 = float(input("Digite a segunda nota: "))

    print('-'*40)
    nota3 = float(input('Digite a terceira nota: '))
    while nota1 < 0:
        print('-'*40)
        print('Nota inválida, digite novamente!')
        nota3 = float(input("Digite a terceira nota: "))

    print('-'*40)
    me = float(input('Digite a nota dos exercícios: '))
    while me < 0:
        print('-'*40)
        print('Nota inválida, digite novamente!')
        me = float(input("Digite a nota dos exercícios: "))


    ma = (nota1 + nota2*2 + nota3*3 + me)/7
    if(ma >= 9,0):
        print('-'*40)
        print(f'Suas notas são: \n Nota1-> {nota1} \n Nota2-> {nota2} \n Nota3-> {nota3} \n Nota dos exercícios-> {me}')
        print(f'O aluno de identificação {id},obteve a média {ma:.2f} e está aprovado com conceito A!')

    if(ma>=7.5 and ma < 9.0):
        print('-'*40)
        print(f'Suas notas são: \n Nota1-> {nota1} \n Nota2-> {nota2} \n Nota3-> {nota3} \n Nota dos exercícios-> {me}')
        print(f'O aluno de identificação {id}, obteve a média {ma:.2f} e está aprovado com conceito B!')

    if(ma>=6 and ma < 7.5):
        print('-'*40)
        print(f'Suas notas são: \n Nota1-> {nota1} \n Nota2-> {nota2} \n Nota3-> {nota3} \n Nota dos exercícios-> {me}')
        print(f'O aluno de identificação {id}, obteve a média {ma:.2f} e está aprovado com conceito C!')

    if(ma>=4 and ma < 6):
        print('-'*40)
        print(f'Suas notas são: \n Nota1-> {nota1} \n Nota2-> {nota2} \n Nota3-> {nota3} \n Nota dos exercícios-> {me}')
        print(f'O aluno de identificação {id}, obteve a média {ma:.2f} e está reprovado com conceito D!')

    if(ma<4):
        print('-'*40)
        print(f'Suas notas são: \n Nota1-> {nota1} \n Nota2-> {nota2} \n Nota3-> {nota3} \n Nota dos exercícios-> {me}')
        print(f'O aluno de identificação {id}, obteve a média {ma:.2f} e está reprovado com conceito E!')
    
    p = input('Deseja cadastrar outro aluno? \n')

    while p.upper()!="SIM" and p.upper()!="NÃO" and p.upper()!="NAO":
        print('-'*40)
        print('Resposta inválida, digite novamente!')
        p = input('Deseja cadastrar outro aluno? \n')