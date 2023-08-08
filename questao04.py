
'''
4) Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na
tela o valor do índice de massa corporal desta pessoa (IMC).
Fórmula: IMC = peso / altura2
 - Obs: peso em quilos e altura em metros
'''
import math

alt = float(input(f"Informe sua altura:"))
pes = float(input(f"Informe seu peso em quilos:"))

imc = pes / math.pow(alt , 2)
print(imc)