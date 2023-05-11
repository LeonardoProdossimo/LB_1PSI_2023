#Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final do mês.

nome = input('Digite o nome do vendedor: ')
sal_fixo = float(input('Digite o salário fixo do vendedor: '))
t_vendas = float(input('Digite o valor tatal de vendas do mês: '))

sal_final = sal_fixo + (t_vendas * 0.15)

print(f'O vendedor {nome} ganhará R$ {sal_final:.2f}')