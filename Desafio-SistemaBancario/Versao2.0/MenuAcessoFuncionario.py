usuarioPreDefinido = "Márcio"
senhaUsuarioPreDefinida = 1234
verificaUsuario = str(input("Digite seu nome de usuário: "))
verificaSenha = int(input("Digite sua senha de usuário: "))

if verificaUsuario == usuarioPreDefinido and verificaSenha == senhaUsuarioPreDefinida:
    print (f"""
----------< Menu >----------
Olá {usuarioPreDefinido}.
Seja bem vindo a nosso sistema bancário.
O que deseja fazer?

1 - Cadastrar Cliente
2 -  Criar Conta de Cliente
""")
else:
    print("Usuário ou senha inválidos.")