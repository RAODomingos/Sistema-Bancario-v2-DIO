import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [lu]\tListar usúarios
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar (saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\nnn Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado í invalido. @@@")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
     excedeu_saldo = valor > saldo
     excedeu_limite = valor > limite
     excedeu_saques = numero_saques >= limite_saques

     if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

     elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

     elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

     elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

     else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

     return saldo, extrato

def exibirExtrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criarUsuario(usuarios):
    cpf = input("Informa o CPF (Somente Númeors): ")
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já Existe usúario com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrarUsuario(cpf, usuarios):
    usuarioFiltrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarioFiltrados[0] if usuarioFiltrados else None

def criarConta(agencia, numeroConta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numeroConta": numeroConta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listarContas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numeroConta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def listarUsuarios(usuarios):
      for usuario in usuarios:
        linha = f"""\
            Nome:\t\t{usuario['nome']}
            CPF:\t\t{usuario['cpf']}
            Data de Nascimento :\t{usuario['data_nascimento']}
            Endereço:\t{usuario['endereco']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 5
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numeroSaques = 0
    usuarios= []
    contas = []


    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input("Informe o valor do Depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Informe o valor de Saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numeroSaques,
                limite_saques=LIMITE_SAQUES,
                
            )
        
        elif opcao == "e":
            exibirExtrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criarUsuario(usuarios)
        
        elif opcao == "lu":
            listarUsuarios(usuarios)

        elif opcao == "nc":
            numeroConta = len(contas) + 1
            conta = criarConta(AGENCIA, numeroConta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listarContas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")



main()