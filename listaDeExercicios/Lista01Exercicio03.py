# O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.

custo_fabrica = float(input('Digite o custo de fabrica do carro: '))

custo_consumidor = custo_fabrica +(custo_fabrica*0.28)  + (custo_fabrica*0.45)

print(f'O custo deste carro ao consumidor é de R$ {custo_consumidor:.2f} ')