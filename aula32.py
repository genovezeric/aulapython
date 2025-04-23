"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro
"""
try:
    numero = int(input('Digite aqui um número inteiro: '))
    if numero % 2 == 0:
        print(f'O número {numero} é par')

    else:
        print(f'O número {numero} é impar')

except:
    print(f'Número informado não é um número inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se em horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18:23 
"""
# try:
#     hora = int(input('Digite aqui a hora: '))
#     maior_dia = hora >= 0
#     menor_dia = hora <= 11
#     maior_tarde = hora >= 12
#     menor_tarde = hora <= 17
#     maior_noite = hora >= 18
#     menor_noite = hora <= 23

#     if maior_dia and menor_noite:
#         if maior_dia and menor_dia:
#             print('Bom dia!')
#         elif maior_tarde and menor_tarde:
#             print('Boa tarde!')
#         elif maior_noite and menor_noite:
#             print('Boa noite!')
    
#     else:
#         print('A hora inserida não é valida, insira um número entre 0 e 23')


# except:
#     print('A hora inserida não é valida')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras
ou menos escreve "Seu nome é curto"; se tiver 5 a 6 letras, escreva "Seu nome é normal",
maior que 6 escreva "Seu nome é muito grande".
"""
try:
    nome = str(input('Digite aqui seu nome: '))
    curto = len(nome) <= 4
    normal = len(nome) == 5 or len(nome) == 6
    longo = len(nome) >= 7

    if curto:
        print('Seu nome é curto!')
    elif normal:
        print('Seu nome é normal!')
    elif longo:
        print('Seu nome é longo')
except:
    print('Nome digitado não é correto')