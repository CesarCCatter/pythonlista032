'''
10) Escreva um algoritmo pergunte o número total de eleitores de um município, o número de votos brancos, nulos
e válidos e apresente como resposta o percentual que cada um representa em relação ao total de eleitores.
'''

ele = int(input("Informe o número de eleitores: "))
vb = int(input("Informe o número de votos brancos"))
vn = int(input("Informe o número de votos nulos"))
vv = int(input("Informe o número de votos válidos"))

pvb = (vb * 100) / ele
pvn = (vn * 100) / ele
pvv = (vv * 100) / ele


print(f"O percentual de votos em branco é: {pvb}")
print(f"O percentual de votos nulos é: {pvn}")
print(f"O percentual de votos válidos é: {pvv}")