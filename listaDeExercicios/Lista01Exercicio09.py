#Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque.

preco = float(input('Digite o preço por litro da gasolina: '))
valor = float(input('Digite o valor a ser gasto com gasolina: '))

q_litros = valor/preco

print(f'Você conseguirá colocar {q_litros} litros de gasolina.')