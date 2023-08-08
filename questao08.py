'''
8) Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda.
Sabese que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.
'''

p = float(input("Informe o preço do produto"))
perc = float(input("Informe o percentual de acréscimo(sem %)"))
vv = p + p *(perc / 100)

print(f"O valor de venda do produto será de: R${vv:.2f}")
