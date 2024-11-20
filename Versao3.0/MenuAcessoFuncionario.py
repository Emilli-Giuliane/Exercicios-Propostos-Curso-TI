usuarioPreDefinido = "Márcio"
senhaUsuarioPreDefinida = 1234

cont = 0
while cont < 3:
    verificaUsuario = str(input("Digite seu nome de usuário: "))
    verificaSenha = int(input("Digite sua senha de usuário: "))
    if verificaUsuario == usuarioPreDefinido and verificaSenha == senhaUsuarioPreDefinida:
        print (f"""
----------< Menu >----------
Olá {usuarioPreDefinido}.
Seja bem vindo a nosso sistema bancário.
if verificaUsuario == usuarioPreDefinido and verificaSenha == senhaUsuarioPreDefinida:
""")
        break
    else:
        cont += 1
        chances = 3 # O único propósito desta variável é para enfeitar o print da linha 22
        if cont == 3:
            print("Você errou 3 vezes, bloqueando usuário e saindo do sistema. . .")
            exit(0)
        print("Usuário ou senha inválidos, você tem ",chances - cont," chances.")

menuResposta =  int(input(f"""
O que deseja fazer?

1 - Cadastrar Cliente
2 -  Criar Conta de Cliente
"""))