#Uma loja de roupas está fazendo uma liquidação e está oferecendo um desconto de 30% em todas as peças. Faça um programa em que o vendedor informe o valor da roupa e o programa retorna quanto ela custará durante a liquidação?

valor = float(input('Digite o valor da roupa: '))

total = valor - (valor * 0.30)
print(f'Essa roupa de R$ {valor:.2f} com desconto passará a custar R$ {total:.2f}')