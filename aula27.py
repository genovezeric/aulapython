"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[5])
print(variavel[-4])
print(variavel[4: ]) # A partir do índice 4 até o final
print(variavel[ :4]) # A partir do índice 4 até o ínicio
print(variavel[4:7]) # A partir do índice 4 até o índice 7

print(len(variavel[4:7]))

print(variavel[0:len(variavel):1]) # Ele printa todos os caracteres sem pular

print(variavel[::-1]) # Ele printa ao contrário a str
print(variavel[-1:-10:-2]) # Ele printa ao contrário a str pulando a cada 2 caracteres