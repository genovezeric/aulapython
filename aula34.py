"""
Repetições
while(enquanto)
Executa uma açõa enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

condicao = True
while condicao:
    nome = input('Qual seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break
print('Acabou')
    