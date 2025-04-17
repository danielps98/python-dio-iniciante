saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

# [d] = Depositar
# [s] = Sacar
# [e] = Extrato
# [q] = Sair


while True:
    print("\n[d] = Depositar\n[s] = Sacar\n[e] = Extrato\n[q] = Sair")

    opcao = input("Escolha uma opção: ").strip().lower()

    if opcao == "d":
        valor = float(input("Informe o valor para depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        valor = float(input("Informe o valor para saque: "))
        if valor > saldo:
            print("Saldo insuficiente.")
        elif valor > limite:
            print("Valor excede o limite por saque.")
        elif numero_saques >= limite_saques:
            print("Número máximo de saques atingido.")

        elif valor > 0:
            saldo -= saldo - valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para saque.")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("==============================")

    elif opcao == "q":
        print("Saindo... Obrigado por usar o sistema bancário!")
        break

    else:
        print("Opção inválida. Tente novamente.")
