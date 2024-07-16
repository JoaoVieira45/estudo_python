dados = []
temp = []
totpessoas = pesomen = pesomai = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(dados) == 0:
        pesomai = pesomen = temp[1]
    else:
        if temp[1] > pesomai:
            pesomai = temp[1]
        if temp[1] < pesomen:
            pesomen = temp[1]
    dados.append(temp[:])
    temp.clear()
    totpessoas += 1
    resp = str(input('Deseja continuar? ')).strip().lower()
    if resp in 'naon':
        break
print(f'Foram introduzidas na lista: \n{dados}')
print(f'Ao todo você cadastrou {totpessoas} pessoas')
print(f'O maior peso foi de {pesomai} peso de ', end='')
for p in dados:
    if p[1] == pesomai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {pesomen} peso de ', end='')
for p in dados:
    if p[1] == pesomen:
        print(f'[{p[0]}] ', end='')