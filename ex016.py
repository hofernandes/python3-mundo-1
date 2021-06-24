# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# import math
from math import (trunc)
num=float(input('Digite um número real: '))
# print(f'O número real {num}, tem como inteiro o número {math.trunc(num)}')
print(f'O número real {num}, tem como número inteiro o {int(num)}')
print(f'O número real {num}, tem como número inteito o {trunc(num)}')
print(f'O número real {num}, tem como número inteiro o {num:.0f}')