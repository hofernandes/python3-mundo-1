# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
# import math
from math import (radians,sin,cos,tan)
angulo=float(input('Digite o Angulo que deseja calcular: '))
#print(f'O valor de seno de {angulo} é {math.sin(math.radians(angulo)):.2f} \nO valor do cosseno de {angulo} é {math.cos(math.radians(angulo)):.2f} \nO valor da tandente de {angulo} é {math.tan(math.radians(angulo)):.2f}')
print(f'O valor de seno de {angulo} é {sin(radians(angulo)):.2f}')
print(f'O valor de cosseno de {angulo} é {cos(radians(angulo)):.2f}3')
print(f'O valor de tangente de {angulo} é {tan(radians(angulo)):.2f}')