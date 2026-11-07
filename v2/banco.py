#sistema bancário
import sys
from operacoes import consultar_saldo, realizar_deposito, realizar_saque, mostrar_extrato, salvar_dados, carregar_dados



opcao = 0
depositos, saques, movimentacoes = carregar_dados()

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
        saldo_atual = consultar_saldo(depositos, saques)
        print(f"Seu saldo é de R$ {saldo_atual:.2f}")
        print("")

    elif opcao == 2:
        while True:
            realizar_deposito(depositos, saques, movimentacoes)

            while True:
                outro_deposito = input("Deseja realizar outro depósito? S/N: ").upper()
                if outro_deposito == "S":
                    break
                elif outro_deposito == "N":
                    break
                else:
                    print("Opção inválida! Digite S ou N")
            if outro_deposito == "N":
                print("")
                break    
                 

    elif opcao == 3:
        while True:
            sucesso =  realizar_saque(depositos, saques, movimentacoes)
            if not sucesso: 
                break
            while True:
                outro_saque = input("Deseja realizar outro saque? S/N: ").upper()
                if outro_saque == "S":
                    break
                elif outro_saque == "N":
                    break
                else:
                    print("Opção inválida! Digite S ou N")
            if outro_saque == "N":
                print("")
                break
                
    elif opcao == 4:
        mostrar_extrato(movimentacoes, depositos, saques,)
        
    elif opcao == 5:
        print("Fechando o programa...")
        sys.exit()

    else:
        print("Opção inválida! Tente novamente:")


    
