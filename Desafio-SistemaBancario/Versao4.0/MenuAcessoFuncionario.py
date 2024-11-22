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
----------< Menu >----------
O que deseja fazer?

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

# Testando se o programa consegue guardar as informações
print(f"""
----------< Analise de Cadastro do Cliente >----------
Nome: {nome}
Idade: {idade}
Telefone fixo e telefone de recado: {telefones[1][0]}, {telefones[1][1]}
Telefone celular: {telCelular}
""")