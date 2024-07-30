matriz = ([0, 0, 0], [0, 0, 0], [0, 0, 0])                                      #crio uma lista com 3 listas de valor 0
spar = mai = scol = 0
for l in range(0, 3):                                                           #for dentro do for para pedir os valores na ordem
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):                                                           #for dentro do for para mostrar os valores na tela
    for c in range(0, 3):                                                       #corretamente
        print(f'[{matriz[l][c]:^5}]', end = '')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-'*20)
print(f'A soma dos pares é {spar}')
print('-'*20)
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos números da coluna três é {scol}')
print('-'*20)
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O número maior da segunda linha é {mai}')