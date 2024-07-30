from random import randint
from time import sleep
print('-' * 10, 'Jogue na Mega Sena', '-' * 10)
lista = list()
jogos = list()
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('~' * 6, f'Sorteando {quant} jogos', '~' * 6)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}:{l}')
    sleep(1)