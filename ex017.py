# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
# import math
from math import hypot
catop=float(input('Digite o valor do cateto oposto: '))
catad=float(input('Digite o valor do cateto adjacente: '))
print(f'O valor da hipotenusa é: {(catop**2+catad**2)**(1/2):.2f}')
# b=pow(catad,2)
print(f'O valor da hipotenusa é: {(pow(catop,2)+pow(catad,2))**(1/2):.2f}')
# print(f'O valor da hipotenusa é: {(math.hypot(catop,catad)):.2f}')
print(f'O valor da hipotenusa é: {hypot(catop,catad):.2f}')