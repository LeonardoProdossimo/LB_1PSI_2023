#A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações.

valor = float(input('Digite o valor da compra: '))
pres = valor/5
print(f'O valor de R$ {valor:.2f} dividido em cinco vezes sem juros é de R$ {pres:.2f}')