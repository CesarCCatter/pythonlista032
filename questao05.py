'''
5) Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
do primeiro pelo segundo número.
'''

num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))

som = num1 + num2
sub = num1 - num2
sub2 = num2 - num1
mult = num1 * num2
div = num1 / num2
rest = num1 % num2

print(f"O resultado da soma dos núneros é: {som}")
print(f"O resultado da subtração do primeiro pelo segundo número é: {sub}")
print(f"O resultado da subtração do segundo pelo primeiro número é:{sub2}")
print(f"O resultado da multilicação dos números é: {mult}")
print(f"O resultado da divisão do primeiro pelo segundo número é: {div}")
print(f"O resto da divisão do primeiro pelo segundo número é: {rest}")

