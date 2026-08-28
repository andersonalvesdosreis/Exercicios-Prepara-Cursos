cliente = ("saque",150,"normal")

match cliente:
    case (tipo,valor,status_contas) if status_contas == "Bloqueada":
        print('Transação recusada: conta bloqueada.')
    case (tipo,valor,status_contas) if (tipo == "saque") and (status_contas == 'normal') and (valor > 5000):
        print('Saque alto detectado. Requer aprovação adicional.')
    case (tipo,valor,status_contas) if (tipo == "saque") and (status_contas == 'suspeita') and (valor > 5000):
        print('Saque bloqueado devido a status de suspeita.')
    case (tipo,valor,status_contas) if (tipo == "saque") and (status_contas == 'suspeita') and (valor > 10000):
        print('Depósito em análise contra lavagem de dinheiro.')
    case (tipo,valor,status_contas) if tipo == 'invalido':
        print('Formato de transação inválido.')
    case _:
        print('Transação realizada com sucesso!')