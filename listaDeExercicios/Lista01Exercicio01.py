# A velocidade média de um veículo é dado pela expressão Vm= ∆S/∆t, onde: 
# ∆S: variação de espaço (ponto de chegada – ponto de partida) em quilômetros
# ∆t: variação de tempo (tempo final – tempo inicial) em horas
# Escreva um programa para calcular a velocidade média dada a variação espacial e a variação temporal.  

import math

ponto1 = float(input("Digite o quilometros inicial: "))
ponto2 = float(input("Digite o quilometros final: "))
tempo1 = float(input("Digite o tempo inicial em horas: "))
tempo2 = float(input("Digite o tempo final em horas: "))
s = ponto2 - ponto1
t = tempo2 - tempo1
Vm =  s/t
print(f'Sua velocidade média é de {Vm}Km/h')




