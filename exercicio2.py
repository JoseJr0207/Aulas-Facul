# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado.Calcule o preço a pagar,sabendo que o 
# carro custa R$ 60 por dia e R$ 0,15 por km rodado. 

km = int(input('Quantos km foram percorridos?'))
dias =int(input('Por quantos dias ele foi alugado?'))

preco = 60 * dias + 0.15 * km 
print('km = {}. Dias: {}'. format(km, dias))
print('Valor a ser pago: {}'.format(preco))
