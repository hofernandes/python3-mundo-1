# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import (sample, shuffle)
n1=str(input('Primeiro Aluno: '))
n2=str(input('Segundo Aluno: '))
n3=str(input('Terceiro Aluno: '))
n4=str(input('Quarto Aluno: '))
print(f'A ordem de apresentação dos trabalos é \33[31m{sample((n1, n2, n3, n4), k=4)}')
lista=[n1, n2, n3, n4]
shuffle(lista)
print(lista)
# print(f'A ordem de apresentação dos trabalhos é {shuffle(n1, n2, n3, n4)}