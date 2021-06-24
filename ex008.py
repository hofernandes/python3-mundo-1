# Estreva um programa que leia um valor em metros e a exiba convertida em centimetros e milimetros
m=float(input('Digite um valor em metros: '))
print('O valor de {} em metros equivale a {}km, {}hm, {}dam, {}dm, {}cm e a {}mm'.format(m,m/1000, m/100, m/10, m*10, m*100, m*1000))