# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-lm sabendo que cada litro de tinta pinta 2m quadrados.
largura=float(input('Qual é a largura da parede? '))
altura=float(input ('Qual é a altura da parede? '))
print(f'Sua parede tem a dimensão de {largura}x{altura} e a área da parede é: {largura*altura:.0f}m² \n Quantidade de tinta é: {largura*altura/2:.3f} litros de tinta')