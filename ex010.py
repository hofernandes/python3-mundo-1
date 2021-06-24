# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos dolares ela pode comprar comptrar.
# Considere US$ 1,00 = R$ 3,27
real=float(input('Digite o valor em reais: R$ '))
dolar=float(5.03)
print(f'O valor em dolares de R$ {real:.2f} é US$ {real/dolar:.2f}')