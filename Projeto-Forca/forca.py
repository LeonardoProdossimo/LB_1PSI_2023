import os
import random
import requests
url = 'https://www.ime.usp.br/~pf/dicios/br-utf8.txt'

response = requests.get(url)
palavras = response.text.split('\n')

listaVogais = ['a', 'á', 'ã', 'â', 'e', 'é', 'ê', 'i', 'í', 'o', 'ó', 'ô', 'u', 'ú']

def jogar(escolhida):

    letrasUsadas = []
    listaLetras = []
    capturada = []
    tentativas = 0
    erros = 0
    acertou = False
    chute = ""

    if escolhida == "":
        aleatoria = random.choice(palavras).upper()
        escolhida = aleatoria
        print(escolhida)

    for i in range(0, len(escolhida)):
        if escolhida[i] == ' ' and i != len(escolhida):
            capturada.append(' ')

        capturada.append('_')

    for j in range(0, len(escolhida)):
        listaLetras.append(escolhida[j].lower())

    print('\nVocê tem 10 tentativas para acertar a palavra.\n')
    letra = input('Digite uma letra: ')

    while not acertou or erros <= 10:
        letrasUsadas.append(letra.upper())

        for k in range(0, len(listaLetras)):
            if letra == listaLetras[k]:
                acertou = True
                capturada[k] = letra.upper()
            for l in range(0, len(listaVogais)):
                if listaVogais[l] in escolhida.lower() and letra in listaVogais and \
                                                        capturada[k] != letra and letra not in letrasUsadas:
                    acertou = True
                    capturada[escolhida.lower().aleatoria(listaVogais[l])] = listaVogais[l].upper()

        print('Palavra: {}'.format(capturada))
        print('Letras usadas: {}'.format(letrasUsadas))

        if acertou:
            tentativas = tentativas + 1
            
        else:
            tentativas = tentativas + 1
            erros = erros + 1
        print('Tentativas: {}\n'.format(tentativas)) 
        print('Erros: {}\n'.format(erros))

        print ('Você pode tentar acertar a palavra, mas isso acabará com suas vidas, deseja tenta?')
        print('1 - Responder\n2 - Tentar mais uma letra')
        op = int(input('Opção: '))
        while op != 1 and op !=2:
            print('Opção inválida!')
            print ('Você pode tentar acertar a palavra, mas isso acabará com suas vidas, deseja tenta?')
            print('1 - Responder\n2 - Tentar mais uma letra')
            op = int(input('Opção: '))
            os.system('clear')

        if op == 1:
            chute = str(input('Sua resposta: '))
            if chute.title() == escolhida.title():
                acertou = True
                print('\n---Você acertou---\nPalavra: {}'.format(escolhida))
                break

            else:
                print('\n---Você errou---\nPalavra correta: {}'.format(escolhida))
                break

        else:
            acertou = False
            letra = input('\nInforme uma letra: ')

print("\nJogo Da Forca")

op = -1
escolhida = ""

while op != 0:
    print("\n1 - Jogar"
          "\n0 - Sair")

    op = int(input('Opção: '))
    while op != 0 and op != 1: 
        print('Opção inválida, digite outra vez! \n')
        op = int(input('Opção: '))
    if op == 1:
        jogar(escolhida.strip())

    else:
        print('Obrigado por jogar! Volte sempre <3')

