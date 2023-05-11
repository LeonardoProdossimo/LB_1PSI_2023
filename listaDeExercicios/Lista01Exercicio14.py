#A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de bolos a cada dia. Cada pãozinho custa R$ 0,12 e o pedaço de bolo custa R$ 1,50. Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e bolos (juntos), e quanto' deve guardar numa conta de poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos para o dono. Com base nestes fatos, faça um algoritmo para ler as quantidades de pães e de bolos vendidos, e depois calcular quanto arrecadou naquele dia e quanto deve guardar na poupança.

pao = int(input('Digite o número de pães vendidos: '))
bolo = int(input('Digite o número de pedaços de bolo vendidos: '))

total = (pao * 0.12) + (bolo * 1.50)
poup = total * 0.10
print(f'O total das vendas do dia é de R$ {total:.2f} e o valor a ser depositado é de {poup:.2f}')