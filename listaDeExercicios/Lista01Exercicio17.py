#Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo vendida respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que o usuário forneça a quantidade de camisetas pequenas, médias e grandes referentes a uma venda, e a máquina informe quanto será o valor arrecadado.

c1 = int(input('Digite o número de camisetas pequenas vendidas: '))
c2 = int(input('Digite o número de camisetas médias vendidas: '))
c3 = int(input('Digite o número de camisetas grandes vendidas: '))

total = (c1 * 10) + (c2 * 12) + (c3*15)
print(f'O valor total arrecadado com as vendas é de R$ {total:.2f}')