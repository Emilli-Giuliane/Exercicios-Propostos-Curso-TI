usuarioPreDefinido = "Márcio"
senhaUsuarioPreDefinida = 1234

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
        chances = 3 # O único propósito desta variável é para enfeitar o print da linha 22
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
2 -  Criar Conta de Cliente
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
    elif menuResposta == 2:
        print("Working in progress. . .")
    elif menuResposta == 0:
        print("Saindo do sistema. . .")
        exit(0)
    else:
        print("")
        print("Opção não existe, por favor escolha entre as opções existentes.")