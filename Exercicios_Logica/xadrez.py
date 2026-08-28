loc = int(input('Digite a posição da L: '))
loc2 = int(input('Digite a posição da C: '))
soma = loc + loc2
print(f'A posição de {loc} e {loc2} é:')
if 1 <= loc and loc2 <= 1000:
    if soma %2 == 0:
        print('Branco')
    else:
        print('Preto')
else:
    print('Fora dos parametros')