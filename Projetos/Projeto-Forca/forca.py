import random
import requests

url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
palavras = []

op = -1
escolhida = ""

def jogar(escolhida):
    letrasUsadas = []
    capturada = ['_'] * len(escolhida)
    tentativas = 1
    erros = 0
    acertou = False

    print('\nVocê tem 10 tentativas para acertar a palavra.\n')

    while not acertou and erros < 10:
        letra = input('Digite uma letra: ').upper()

        if letra in letrasUsadas:
            print("Você já usou essa letra. Tente outra.")
            continue

        letrasUsadas.append(letra)

        if letra in escolhida:
            for i in range(len(escolhida)):
                if escolhida[i] == letra:
                    capturada[i] = letra
            acertou = '_' not in capturada
        else:
            erros += 1
        print('\nTentativas: {}'.format(tentativas) + '\nErros: {}'.format(erros)) 
        print('Palavra: {}'.format(' '.join(capturada)))
        print('Letras usadas: {}'.format(letrasUsadas))
        tentativas = tentativas + 1
    if acertou:
        print('Você acertou---\nPalavra: {}'.format(escolhida))
    else:
        print('Você errou---\nPalavra correta: {}'.format(escolhida))

print('-' * 40)
print("\nJogo Da Forca")

print("\n1 - Jogar"
      "\n0 - Sair")

op = int(input('Opção: '))
while op != 0 and op != 1:
    print('Opção inválida, digite outra vez! \n')
    op = int(input('Opção: '))

if op == 1:
    response = requests.get(url)
    palavras = response.text.split('\n')
    escolhida = random.choice(palavras).upper()
    jogar(escolhida)
else:
    print('Obrigado por jogar! Volte sempre <3')
