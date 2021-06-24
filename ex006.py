# Crie um algoritimo que leia um número e mostr o seu dobro, triplo e raiz quadrada
num=int(input('Digite um número: '))
print('O dobro de {} é {} \n O triplo de {} é {} \n A raiz quadrada de {} é {} ou {}'.format(num,num*2,num,num*3,num,num**(1/2),pow(num,1/2)))