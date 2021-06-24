# Faça um programa que leia o salário de um funcionário e mostre seu novo salário com um aumento de 15%
salario=float(input('Digite o seu salário: '))
print('Você recebia R$ {:.2f} com um aumento de 15% você vai receber R$ {:.2f}'.format(salario,salario+salario*15/100))