cliente = ("saque", 150, "normal")

match cliente:
    case (_, _, "bloqueada"):
        print("Transação recusada: conta bloqueada.")
    case ("saque", valor, "normal") if valor > 5000:
        print("Saque alto detectado. Requer aprovação adicional.")
    case ("saque", _, "suspeita"):
        print("Saque bloqueado devido a status de suspeita.")
    case ("deposito", valor, "suspeita") if valor > 10000:
        print("Depósito em análise contra lavagem de dinheiro.")
    case (("saque" | "deposito"), valor, ("normal" | "suspeita")) if valor > 0:
        print("Transação realizada com sucesso!")
    case _:
        print("Formato de transação inválido.")