# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km=float(input('Quantos KM foram percorridos? '))
dias=int(input('Quantos dias o carro foi alugado? '))
print (f'Por ter alugado o carro por {dias} dias e percorrido {km} KM, o preço a pagar é de: R$ {dias*60+km*0.15:.2f}')