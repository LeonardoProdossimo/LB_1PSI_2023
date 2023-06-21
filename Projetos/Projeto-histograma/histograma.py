dias = ['DOMINGO','SEGUNDA','TERÇA','QUARTA','QUINTA','SEXTA','SABADO']
ast = []
temps= []

def inicio():
    for i in range(len(dias)):
        temp = int(input(f'Digite a temperatura de {dias[i].lower()}: \n'))
        while temp <0 or temp > 80:
            print('Tempertura inválida, digite novamente!')
            temp = int(input(f'Digite a temperatura média de {dias[i].lower()}: \n'))
        aste = '*' * temp
        ast.append(aste)
        temps.append(temp)   

def grafico():
    print('-' * 40)
    for j in range(len(dias)):
        dia = dias[j]
        print(f'{dia[0]}-> {temps[j]}C°: {ast[j]}')

print('-' * 40)
print("Histograma")
print("Deseja registrar as temperaturas médias da semana?")

print("\n1 - Sim"
      "\n0 - Sair")

op = int(input('Opção: '))
while op != 0 and op != 1:
    print('Opção inválida, digite outra vez! \n')
    op = int(input('Opção: '))

if op == 1:
    inicio()
    grafico()
else:
    print('Obrigado! Volte sempre <3')



