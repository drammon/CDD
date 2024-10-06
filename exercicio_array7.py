tamanho = 3
bloqueados = []

nomes = [""]*tamanho
senhas = [""]*tamanho
cpf = [""]*tamanho

acesso = False

tentativas = 3
opcao = 0

while opcao != 5:
    opcao = int(input(" 1: Cadastro;\n 2: Log-in;\n 3: Mostrar todos os usuários, senhas e bloqueados;\n 4: Desbloquear conta;\n 5: Sair.\n\n Escolha: "))

    match opcao:
        case 1:
            for i in range(tamanho):
                nomes[i] = input(f"Cadastre o nome do {i + 1}º usuário: ")
                senhas[i] = input(f"Cadastre a senha do {i + 1}º usuário: ")
                cpf[i] = input(f"Informe o CPF do {i + 1}º usuário (apenas números): ")

        case 2:

            while tentativas > 0:
                nome_tentativa = input("Insira seu nome de usuário: ")

                if nome_tentativa in bloqueados:
                    print("Sua conta está bloqueada. Acesse o item 4 para desbloquear sua conta.")
                    break

                if nome_tentativa not in nomes:
                    print("Este usuário ainda não está cadastrado.")
                    break

                senha_tentativa = input("Insira sua senha: ")


                for i in range(tamanho):

                    if nomes[i] == nome_tentativa and senhas[i] == senha_tentativa:
                        acesso = True


                if acesso == False:
                    tentativas -= 1
                    print(f"Senha e/ou Nome de Usuário incorretos! Você tem {tentativas} tentativas.")

                else:
                    print("Log-in realizado com sucesso!")
                    acesso = False
                    tentativas = 3
                    break

                if tentativas == 0:
                    print("Conta bloqueada!")
                    bloqueados += nome_tentativa
                    tentativas = 3
                    acesso = False
                    break

        case 3:
            print(nomes, senhas, cpf)
            print(bloqueados)
            for i in range(tamanho):
                print(f" Nome: {nomes[i]}, Senha: {senhas[i]}, CPF: {cpf[i]}, Posição: {i}")

        case 4:
            restaura = False

            while restaura == False:

                nome_tentativa = input("Insira seu nome de usuário: ")

                if nome_tentativa not in nomes:
                    print("Este usuário ainda não está cadastrado.")
                    break

                cpf_tentativa = input("Insira seu CPF (apenas números): ")


                for i in range(tamanho):

                    if nomes[i] == nome_tentativa and cpf[i] == cpf_tentativa:

                        for x in range(len(bloqueados)):
                            if bloqueados[x] == nome_tentativa:
                                bloqueados[x] = ""
                                restaura = True


        case 5:
            break
