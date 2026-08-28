#cliente = (12,200)
cliente = (20,90)

match cliente:
    case (idade,valor) if (idade <= 12 or idade >= 65) and (valor > 100):
        print(f'Parabens pela compra\nVocê tem {idade} e comprou R${valor} em compras\nGanhou 20% de desconto\nValor final da compra R${valor-(valor*0.20)}')
    case (idade,valor) if idade <= 12 or idade >= 65:
        print(f'Parabens pela compra\nVocê tem {idade} e comprou R${valor} em compras\nGanhou 10% de desconto\nValor final da compra R${valor-(valor*0.10)}')
    case _:
        print(f'Parabens pela compra\nVocê tem {idade} e comprou R${valor} em compras\nValor final da compra R${valor}')