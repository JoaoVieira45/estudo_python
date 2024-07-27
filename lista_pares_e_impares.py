print('-'*21)
print('Lista pares e ímpares')
print('-'*21)
num = ([], [])                                                          #crio a lista com 2 lista, onde a primeira é dos números
valor = 0                                                               #pares e a segunda é dos ímpares
count = 0
for c in range(0, 7):
    valor = (int(input(f'Digite o {count+1} número: ')))
    count += 1
    if valor % 2 == 0:                                                  #faço a soma e adiciono os pares e o ímpares nas respectivas listas
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()                                                           #com o comando sort eu organizo as listas
num[1].sort()
print('-='*20)
print(f'Os números pares são: {num[0]}')
print(f'Os valores ímpares são {num[1]}')