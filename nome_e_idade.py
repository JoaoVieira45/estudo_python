gal = list()
dado = list()
totmaior = totmenor = 0
for c in range(0, 5):
    dado.append((str(input('Nome: '))))
    dado.append(int(input('Idade: ')))
    gal.append(dado[:])
    dado.clear()

for p in gal:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor +=1
print(f'Temos {totmaior} maior de idade e {totmenor} menor de idade')