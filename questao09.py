'''
9) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas
em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias.
'''

ano = int(input("Informe a sua idade: "))
mes = int(input("Quantos meses faz desde que você fez aniversário?"))
dia = int(input("Quantos dias faz desde que você fez um 'mesversário'?"))

anod = ano * 365
mesd = mes * 30

diad = anod + mesd + dia
print(f"Você tem {diad} dias de idade")