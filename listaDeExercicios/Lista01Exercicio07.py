#Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados. Ex: Início A vale 3 e B vale 5 no final da execução A valerá 5 e B valerá 3.

a = int(input('Digite o valor  de A: '))
b = int(input('Digite o valor de B: '))

v_A = a
a = b


print(f'O valor de A agora é: {a} e o valor de B agora é {v_A}')
