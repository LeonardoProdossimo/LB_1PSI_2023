#O restaurante a quilo Bem-Bão cobra R$19,00 por cada quilo de refeição. Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e escreva o valor a pagar. Assuma que a balança já desconte o peso do prato.

quilo = float(input("Digite quantos quilos deu o seu prato: "))
valor = quilo * 19

print(f'O valor da sua refeição é de R$ {valor:.2f}')