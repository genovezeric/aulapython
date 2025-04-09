# Desafio 3 
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

numero1 = int(primeiro_valor)
numero2 = int(segundo_valor)

if numero1 > numero2:
    print(f'Primeiro valor:{numero1} é maior que Segundo Valor:{numero2}')

elif numero1 < numero2:
    print(f'Segundos valor:{numero2} é maior que o Primeiro Valor:{numero1}')

elif numero1 == numero2:
    print(f'Primeiro valor:{numero1} é igual ao Segundo Valor:{numero2}')

else:
    print(f'Não foi inserido nenhum valor numérico!')