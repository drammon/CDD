nomes = [""]*5
senhas = [""]*5
tam = len(nomes)

opcao = 0
while opcao != 4:
    opcao = int(input(" 1: Cadastro;\n 2: Login;\n 3: Mostrar todos os usuários;\n 4: Sair\n Escolha: "))

    match opcao:
        case 1:
            for i in range(tam):
                nomes[i] = input(f"Cadastre o nome do {i + 1}º usuário: ")
                senhas[i] = input(f"Cadastre a senha do {i + 1}º usuário: ")

        case 2:

            tentativas = 3

            while tentativas > 0:
                nome_try = input("Insira seu nome de usuário: ")
                senha_try = input("Insira sua senha: ")

                for i, e in enumerate(nomes):
                    if nomes[e] == nome_try and senhas[e] == senha_try and nomes[i] == senhas[i]:
                        print("Log-in realizado com sucesso!")
                        break
                    else:
                        tentativas -= 1
                        print(f"Senha incorreta! Tente novamente mais {tentativas} vezes.")
            if tentativas == 0:
                print("Conta bloqueada!")
        case 3:

            for i in range(tam):
                print(f" Nome: {nomes[i]}, Senha: {senhas[i]}, Posição: {i}")

        case 4:
            break