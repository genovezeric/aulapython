"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro
"""
try:
    numero = int(input('Digite aqui um número inteiro: '))
    if numero % 2 == 0:
        print(f'O número: {numero} é par')

    else:
        print(f'O número: {numero} é impar')

except:
    print('Este não é um número inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se em horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18:23 
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras
ou menos escreve "Seu nome é curto"; se tiver 5 a 6 letras, escreva "Seu nome é normal",
maior que 6 escreva "Seu nome é muito grande".
"""