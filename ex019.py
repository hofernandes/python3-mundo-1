# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import sample, choice
aluno1=str(input('Nome do primeiro aluno: '))
aluno2=str(input('Nome do segundo aluno: '))
aluno3=str(input('Nome do terceuro aluno: '))
aluno4=str(input('Nome do quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
print({choice(lista)})
# r=sample([aluno1, aluno2, aluno3, aluno4],k=1)
# print(f'O aluno escolhido foi {r}')
print(f'O aluno escolhido foi {sample((aluno1, aluno2, aluno3, aluno4),k=1)}')