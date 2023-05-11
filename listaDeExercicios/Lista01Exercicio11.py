#Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês. Considere fixo o juro da poupança em 0,70% a. m.

valor_depositado = float(input('Digite o valor depositado: '))
ren_mes = valor_depositado + (valor_depositado*0.07)
print(f'O valor do seu deposito com redimento após um mês é de R$ {ren_mes:.2f} ')