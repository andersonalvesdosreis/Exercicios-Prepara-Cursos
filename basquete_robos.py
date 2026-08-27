from rich import print
D_distancia = int(input('Digite a distancia: '))
pontos = 0
if D_distancia <= 800:
    pontos = 1
elif 800 < D_distancia <= 1400:
    pontos = 2
elif 1400 < D_distancia:
    pontos = 3
print(f'{D_distancia} -->  {pontos} Pontos')