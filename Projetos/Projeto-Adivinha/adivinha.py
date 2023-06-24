import random as r
rep = True

while rep:
    def adivinha():
        listaNumeros=[]
        tentativas = 1
        num = r.randint(1,101)
        print('-'*40)
        print('Regras: ')
        print('O programa irá escolher um número aleatório entre 1 e 100.')
        print('O jogador tem no máximo 10 tentativas.')
        print('O jogador faz uma suposição fornecendo um número.')
        print('O programa irá informa ao jogador se o número correto é maior ou menor do que a suposição feita.')
        print('O jogador continua fazendo suposições até adivinhar corretamente o número ou esgotar o número de tentativas.')
        while tentativas != 11:
            print('-'*40)
            chute = int(input('Digite um número de 1 à 100: \n'))
            while chute <=0 or chute >100:
                print('Número inválido, digite novamente!')
                chute = int(input('Digite um número de 1 à 100: \n'))
            if(chute < num):
                print('Número aleatório é maior que seu chute!')
                print('-'*40)
            elif(chute > num):
                print('Número aleatório é menor que seu chute!')
                print('-'*40)
            elif(chute == num):
                print(f'Parabéns você acertou! \n Com o montante de {tentativas} tentativas!')
                print('-'*40)
                break
            else:
                print(f'Que pena você errou todos os seus chutes e chegou no total de {tentativas} tentativas!')
                print('-'*40)
                break
            listaNumeros.append(chute)
            print(f'Números usados: {listaNumeros}')
            tentativas += 1
            print('-' * 40)

    print("\nBem-vindo ao jogo do adivinho! Digite a opção para prosseguir!")
    print("\n1 - Jogar"
        "\n0 - Sair")

    op = int(input('Opção: '))
    while op != 0 and op != 1:
        print('Opção inválida, digite outra vez! \n')
        op = int(input('Opção: '))

    if op == 1:
        adivinha()
    else:
        print('Obrigado por jogar! Volte sempre <3')
        rep = False
       
    
