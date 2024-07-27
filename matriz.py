matriz = ([0, 0, 0], [0, 0, 0], [0, 0, 0])                                      #crio uma lista com 3 listas de valor 0
for l in range(0, 3):                                                           #for dentro do for para pedir os valores na ordem
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):                                                           #for dentro do for para mostrar os valores na tela
    for c in range(0, 3):                                                       #corretamente
        print(f'[{matriz[l][c]:^5}]', end = '')
    print()
