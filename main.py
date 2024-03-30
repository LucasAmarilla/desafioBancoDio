menu = """
[d] Depositar
[s] Sacar
[d] Extrato
[d] sair


"""


saldo = 0
limite = 0 
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor de deposito"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito de: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor digitado parece ser invalido")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        sem_saldo = valor > saldo

        sem_limite = valor > limite

        sem_saques = numero_saques >= LIMITE_SAQUES

        if sem_saldo:
            print("Ta duro dorme! sem saldo na conta!")
        elif sem_limite:
            print("Ta duro dorme! sem limite na conta!")
        elif sem_saques:
            print("Parece que voce antigiu o limite de saques de hoje, tente novamente em outro horario")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else: 
            print("Operação falhou, digite um valor valido")

    elif opcao == "e":
        print("\n============EXTRATO================")
        print("Sem movimentos "if not extrato else extrato)
        print(f"Saldo final: R${saldo:.2f}")
        print("\n==================================")

    elif opcao == "q":
        break

    else:
        print("Informe uma opção valida!!")
        