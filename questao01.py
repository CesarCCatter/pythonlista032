'''
Criar um projeto no PyCharm chamado PythonLista032.
Fazer cada questão da lista em um arquivo python (questao01.py, questao02.py ...).
Incluir em cada arquivo o enunciado da questão comentário de bloco.
Utilizar os recursos de Interpolação de Strings e Operadores para resolver as questões.
Publique este projeto no seu GitHub e coloque a URL dele na atividade FTI 02 no teams
'''

'''1) Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o 
valor com o acréscimo dos 10% da gorjeta do garçom.'''

conta = float(input("Qual o valor da conta? R$"))
garcom = conta + (conta * 0.10)

print(f"O valor da conta com o acréscimo de 10% do garçom é de: R${garcom:.2f}")