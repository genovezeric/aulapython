# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 
#  J o ã o
# -4-3-2-1

# nome = 'João'
# print(nome[2])
# print(nome[-2])

# print('ão' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('ão' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
find = input('Digite o que deseja encontrar: ')

if find in nome:
    print(f'{find} está em {nome}')
else:
    print(f'{find} não está em {nome}')