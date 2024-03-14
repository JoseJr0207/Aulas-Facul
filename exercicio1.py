# Desenvolva um algoritimo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele.
# calcule e exiba o valor do desconto e o preço final do produto 

preco = float(input('digite o preço do produto:'))
p = float(input('digite o percentual de desconto (0-100)%:'))

desconto = preco * (p / 100)
final = preco - desconto 

print('O preço do produto é {}. Desconto de {}%.'.format(preco, p))
print('Valor calculado de desconto: {}. Valor final do produto: {}'.format(desconto, final))

