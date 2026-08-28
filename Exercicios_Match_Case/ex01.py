temp = 32

match temp:
    case clasificar_temp if clasificar_temp < 10:
        print('Muito Frio!')
    case clasificar_temp if clasificar_temp > 30:
        print('Muito quente!')
    case _:
        print('Normal!')

