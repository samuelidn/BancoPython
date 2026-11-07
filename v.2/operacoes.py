import json
import os
CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), "dados_banco.json")

#Funções

#Consultar o saldo

def consultar_saldo(depositos, saques):
    saldo = sum(depositos) - sum(saques)
    return saldo

#Fazer o depósito

def realizar_deposito(depositos, saques, movimentacoes):
    try:
        deposito = float(input("Digite o valor do depósito: "))
    except ValueError:
        print("Valor inválido! Digite apenas números.")
        return
    if deposito <= 0:
        print("O valor precisa ser positivo")
        return
    
    depositos.append(deposito)
    movimentacoes.append({
        "tipo": "Depósito",
        "valor": deposito
    })
    salvar_dados(depositos, saques, movimentacoes)
    print(f"Depósito de R$ {deposito:.2f} processado com sucesso!")

#Fazer o saque

def realizar_saque(depositos, saques, movimentacoes):
    saldo_atual = consultar_saldo(depositos, saques)
    if saldo_atual <= 0:
        print("Você não possui saldo disponível para saque.")
        return False
    try:
        saque = float(input("Digite o valor do saque: "))
    except ValueError:
        print("Valor inválido! Digite apenas números")
        return False
    
    if saque > saldo_atual:
        print(f"Saldo insuficiente! Seu saldo é de: R$ {saldo_atual}")
        return False
    elif saque <= 0:
        print("O valor precisa ser positivo")
        return False
    
    saques.append(saque)
    movimentacoes.append({
        "tipo": "Saque",
        "valor": saque
    })
    salvar_dados(depositos, saques, movimentacoes)
    print(f"Saque no valor de R$ {saque:.2f} realizado com sucesso!")
    return True

#Mostrar o extrato

def mostrar_extrato(movimentacoes, depositos,saques):
    saldo_atual = consultar_saldo(depositos, saques)
    print("==== SEU EXTRATO BANCÁRIO ====")

    for movimentacao in movimentacoes:
        print(f"{movimentacao["tipo"]}: R$ {movimentacao["valor"]:.2f}")
            
    print("")
    print(f"Saldo atual: R$ {saldo_atual:.2f} ")
    print("")


#Salvar os dados

def salvar_dados(depositos, saques, movimentacoes):
    dados = {
        "depositos": depositos,
        "saques": saques,
        "movimentacoes": movimentacoes
    }

    with open("CAMINHO_ARQUIVO", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4)

def carregar_dados():
    try:
        with open("CAMINHO_ARQUIVO", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        return dados["depositos"], dados["saques"], dados["movimentacoes"]

    except FileNotFoundError:
        return [], [], []