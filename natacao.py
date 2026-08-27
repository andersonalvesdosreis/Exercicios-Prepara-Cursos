lista_tmp = []
def tempo():
    for n in range(0,3):
        tmp = int(input('Digite o tempo: '))
        lista_tmp.append(tmp)
tempo()
lista_tmp.sort()
print(f'Primeiro Lugar: {lista_tmp[0]}\nSegundo Lugar: {lista_tmp[1]}\nTerceiro Lugar: {lista_tmp[2]}')