# f-strings
# Formatar a mensagem do desafio

nome = 'Joao Silva'
altura = 1.80
peso = 95   
imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos, e seu IMC é'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)

# print(nome, 'tem', altura, 'de altura,')
# print('pesa', peso, 'quilos e seu IMC é')
# print(imc)

# A fórmula é IMC = peso / (altura x altura)