# Menu de acesso de funcionários
# variaveis

usuarioPreDefinido = "Márcio"
senhaUsuarioPreDefinida = 1234
cadastroCliente = False # Esta variável verifica se existe cadastro de cliente feito anteriormente

cont = 0
while cont < 3:
    verificaUsuario = str(input("Digite seu nome de usuário: "))
    verificaSenha = int(input("Digite sua senha de usuário: "))
    if verificaUsuario == usuarioPreDefinido and verificaSenha == senhaUsuarioPreDefinida:
        print (f"""
----------< Principal >----------
Olá {usuarioPreDefinido}.
Seja bem vindo a nosso sistema bancário.""")
        break
    else:
        cont += 1
        chances = 3 # O único propósito desta variável é para enfeitar o print da linha 24
        if cont == 3:
            print("Você errou 3 vezes, bloqueando usuário e saindo do sistema. . .")
            exit(0)
        print("Usuário ou senha inválidos, você tem ",chances - cont," chances.")

while True:
    menuResposta =  int(input(f"""
----------< Menu >----------
O que deseja fazer?

0 - Sair
1 - Cadastrar Cliente
2 - Criar Conta de Cliente
"""))

    if menuResposta == 1:
        print(f"""
----------< Cadastrar Cliente >----------
Favor preencher com os seguintes dados requiridos >>>
"""    )
        nome = str(input("Informe o nome do cliente: "))
        idade = int(input("Informe a idade do cliente: "))
        telefones = [input("Digite o numero de celular: "),[input("Digite o número de telefone fixo: "),input("Digite o número de telefone de recado: ")]]
        telCelular = telefones[0] #testando se consegui usar o telefone celular apartir de uma variável
        cadastroCliente = True
    elif menuResposta == 2:
        if cadastroCliente == True:
            print(f"""
----------< Criar conta de Cliente >----------""")
            emailCliente = str(input("Informe o email: "))
            novaSenhaCliente = int(input("Digite uma senha com números inteiros: "))
            conferirNovaSenhaCliente = int(input("Digite sua senha novamente: "))
            if novaSenhaCliente == conferirNovaSenhaCliente:
                print("Senha guardada com sucesso! Te levaremos ao menu do cliente. Aguarde. . .")
                break
            else:
                print("Senhas não correspondem, tente criar uma senha novamente.")
        else:
            print("É necessário possuir um cadastro do Cliente para criar a conta no banco.")
    elif menuResposta == 0:
        print("Saindo do sistema. . .")
        exit(0)
    else:
        print("")
        print("Opção não existe, por favor escolha entre as opções existentes.")

# Variaveis
saldo = 0.0
sacar = 0.0
depositar = 0.0
historicoSacar = []
historicoDepositar = []

# Menu de Saque e depósito do cliente
while True:
    MenuClienteResposta = int(input(f"""
----------< Menu do Cliente >----------
Bem-vindo {nome}, é um prazer atendê-lo. Como podemos te ajudar hoje?

0 - Sair do Sistema
1 - Verificar Saldo
2 - Sacar
3 - Depositar
4 - Ver histórico
    """))
    if MenuClienteResposta == 0:
        print("Fechando o sistema. . .")
        exit(0)
    elif MenuClienteResposta == 1:
        print("Seu saldo é de: R$",saldo)
    elif MenuClienteResposta == 2:
        sacar = float(input("Infome o valor que deseja sacar: "))
        if saldo >= sacar:
            saldo = saldo - sacar
            historicoSacar.append(sacar)
        else:
            print("Você não pode sacar um valor mais alto que seu saldo.")
    elif MenuClienteResposta == 3:
        depositar = float(input("Informe o valor a ser depositado: "))
        saldo = depositar + saldo
        historicoDepositar.append(depositar)
    elif MenuClienteResposta == 4:
        print("Seu histórico de saques: ",historicoSacar)
        print("Seu histórico de depósitos: ",historicoDepositar)
    else:
        print("")
        print("Opção não existe, por favor escolha entre as opções existentes.")