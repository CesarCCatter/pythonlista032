'''
3) Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros.
'''

alt = float(input(f"Informe sua altura:"))
pes = float(input(f"Informe seu peso em quilos:"))

altcm = alt * 100
pesg = pes * 1000

print(f"Sua altura em centímetros é {altcm}cm")
print(f"Seu peso em gramas é {pesg}g")
