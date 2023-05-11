#Faça um algoritmo para ler o salário de um funcionário e aumentá-Io em 15%. Após o aumento, desconte 8% de impostos. Imprima o salário inicial, o salário com o aumento e o salário final.

sal = float(input('Digite o seu salário atual: '))
sal1 = sal * 0.15 + sal
sal2 = sal1 - sal1 * 0.08
print(f'O seu salário era de R$ {sal:.2f} com o aumento de 15% ficou R$ {sal1:.2f}, mas descontando o imposto de 8% será de R$ {sal2:.2f}')