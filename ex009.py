# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
n=int(input('Digite um número que deseja calculcar a tabuada: '))
print('A tabuada de {} é:' )
print('='*20)
print('  0  x {:3} = {:3} \n  1  x {:3} = {:3} \n 2x{:3}={:3} \n 3x{:3}={:3} \n 4x{:3}={:3} \n 5x{:3}={:3} \n 6x{:3}={:3} \n 7x{:3}={:3} \n 8x{:3}={:3} \n 9x{:3}={:3} \n 10x{:3}={:3}'.format(n,n,n*0,n,n*1,n,n*2,n,n*3,n,n*4,n,n*5,n,n*6,n,n*7,n,n*8,n,n*9,n,n*10))
print('='*20)
print(f'{n:<3} x {0:3} = {n*0:>3}')
print(f'{n:<3} x {1:3} = {n*1:>3}')
print(f'{n:<3} x {2:3} = {n*2:>3}')
print(f'{n:<3} x {3:3} = {n*3:>3}')
print(f'{n:<3} x {4:3} = {n*4:>3}')
print(f'{n:<3} x {5:3} = {n*5:>3}')
print(f'{n:<3} x {6:3} = {n*6:>3}')
print(f'{n:<3} x {7:3} = {n*7:>3}')
print(f'{n:<3} x {8:3} = {n*8:>3}')
print(f'{n:<3} x {9:3} = {n*9:>3}')
print(f'{n:<3} x {10:3} = {n*10:>3}')
print('='*20)