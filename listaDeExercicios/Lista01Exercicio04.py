# Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto

dis_percorrida = float(input('Digite a diatância percorrida em quilometros: '))
listros_gastos = float(input('Digite a quantidade gasta de litros: '))

consumo_medio = dis_percorrida/listros_gastos
print(f'O consumo médio do seu carro é de {consumo_medio} quilometros por litro de combustível.')
