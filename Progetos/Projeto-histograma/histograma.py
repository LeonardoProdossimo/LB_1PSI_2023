dias = ['DOMINGO','SEGUNDA','TERÇA','QUARTA','QUINTA','SEXTA','SABADO']
ast = []
temps= []

for i in range(len(dias)):
    temp = int(input(f'Digite a temperatura de {dias[i].lower()}: \n'))
    while temp <0 or temp > 80:
        print('Tempertura inválida, digite novamente!')
        temp = int(input(f'Digite a temperatura média de {dias[i].lower()}: \n'))
    aste = '*' * temp
    ast.append(aste)
    temps.append(temp)   

for j in range(len(dias)):
    dia = dias[j]
    print(f'{dia[0]}-> {temps[j]}C°: {ast[j]}')


