'''
7) A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que
pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das
prestações.
'''

val = float(input("Informe o valor da sua compra: R$"))
prest = int(input("Quantas prestações foram escolhidas?"))

print(f"O valor das prestações será de: R${val / prest:.2f}")