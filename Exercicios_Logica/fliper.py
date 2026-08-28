escolha1 = int(input('Digite a primeira escolha: (0 ou 1) '))
escolha2 = int(input('Digite a segunda escolha: (0 ou 1) '))
lista = [escolha1,escolha2]
print(f'Suas escolhas: {lista}')
match lista:
    case [0,0]:
        print('C')
    case [1,0]:
        print('B')
    case [0,1]:
        print('A')
    case [1,1]:
        print('A')
