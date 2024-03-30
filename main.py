
def menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [d] Extrato
    [nu] Novo usuario
    [nc] Novo conta
    [d] sair

    """

    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
                saldo += valor
                extrato += f"Deposito de: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor digitado parece ser invalido")
    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: "))
            
    sem_saldo = valor > saldo

    sem_limite = valor > limite

    sem_saques = numero_saques >= limite_saques

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

    return saldo, extrato

def show_extrato(saldo, /, *, extrato):
        print("\n============EXTRATO================")
        print("Sem movimentos "if not extrato else extrato)
        print(f"Saldo final: R${saldo:.2f}")
        print("\n==================================")

def crate_user(usuarios):
    cpf = float(input("Informe o cpf: "))
    usuario = filtrar_user(cpf, usuarios)

    if usuario: 
         print("Usuario existente!! ")
    nome = input("Informe o nome do usuario: ")
    nascimento = input("Informe a data de nascimento do usuario: ")

    usuarios.append({"nome:": nome, "nascimento:": nascimento, "cpf":cpf})

def create_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuario")
    usuario = filtrar_user(cpf, usuarios)

    if usuarios:
         print("Conta criada com sucesso!")
         return {"agencia:": agencia, "numero da conta": numero_conta, "usuario: ": usuario}
    
    
    

def filtrar_user(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None
     
     

def main():
    saldo = 0
    limite = 0 
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []


    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor de deposito"))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor de saque"))
            saldo, extrato = saque(saldo = saldo, valor = valor, extrato = extrato, limite = limite, numero_saques = numero_saques, limite_saques = LIMITE_SAQUES)

        elif opcao == "e":
            show_extrato(saldo, extrato=extrato) 
        
        elif opcao == "nu":
            crate_user(usuarios) 

        elif opcao == "nc":
            nro_conta = len(contas)+1
            conta = create_conta(AGENCIA, nro_conta, usuarios)

            if conta:
                 conta.append(conta)

        elif opcao == "q":
            break

        else:
            print("Informe uma opção valida!!")

main()