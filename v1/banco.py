#sistema bancário
import sys

opcao = 0
depositos = []
saques = []


while True:
    print("========== BANCO PYTHON ==========")
    print("")
    print("1 - Consultar saldo\n2 - Depositar\n3 - Sacar\n4 - Extrato\n5 - Sair\n")

    try:
        opcao = int(input("Digite qual opção deseja acessar: "))
    except ValueError:
        print("Opção inválida! Digite apenas números.")
        continue


    if opcao == 1:
        saldo_atual = sum(depositos) - sum(saques)
        print(f"Seu saldo é de: R$ {saldo_atual:.2f}")
        print("")

    elif opcao == 2:
        while True:
            try:
                deposito = float(input("Digite o valor do depósito: "))
            except ValueError:
                print("Valor inválido! Digite apenas números.")
                continue

            if deposito <= 0:
                print("O valor precisa ser positivo")
                continue
        
            depositos.append(deposito)

            print(f"Depósito de R$ {deposito:.2f} processado com sucesso!")

            while True:
                outro_deposito = input("Deseja realizar outro depósito? S/N: ").upper()
                if outro_deposito == "S":
                    break
                elif outro_deposito == "N":
                    break
                else:
                    print("Opção inválida! Digite S ou N")
            if outro_deposito == "N":
                break    
                print("")

    elif opcao == 3:
        while True:
            saldo_atual = sum(depositos) - sum(saques)
            try:
                saque = float(input("Digite o valor do saque: "))
            except ValueError:
                print("Valor inválido! Digite apenas números")
                continue

            if saque > saldo_atual:
                print(f"Saldo insuficiente! Seu saldo é de: R$ {saldo_atual}")
                continue
            elif saque <= 0:
                print("O valor precisa ser positivo")
                continue

            saques.append(saque)
            print(f"Saque no valor de R$ {saque} realizado com sucesso!")
            while True:
                outro_saque = input("Deseja realizar outro saque? S/N: ").upper()
                if outro_saque == "S":
                    break
                elif outro_saque == "N":
                    break
                else:
                    print("Opção inválida! Digite S ou N")
            if outro_saque == "N":
                break
                print("")
        
    elif opcao == 4:
        saldo_atual = sum(depositos) - sum(saques)
        print("==== SEU EXTRATO BANCÁRIO ====")
        for valor in saques:
            print(f"Saque: R$ {valor:.2f}")

        for valor2 in depositos:
            print(f"Depósito: R$ {valor2:.2f}")
        
        print("")
        print(f"Saldo atual: R$ {saldo_atual:.2f} ")
        print("")
    elif opcao == 5:
        print("Fechando o programa...")
        sys.exit()

    else:
        print("Opção inválida! Tente novamente:")
