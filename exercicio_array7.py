import biblioteca

tamanho = 3
bloqueados = []

nomes = [""]*tamanho
senhas = [""]*tamanho
cpf = [""]*tamanho

acesso = False

tentativas = 3
opcao = ""

while opcao != "5":
    opcao = input(" 1: Cadastro;\n 2: Log-in;\n 3: Mostrar todos os usuários, senhas e bloqueados;\n 4: Desbloquear conta;\n 5: Sair.\n\n Escolha: ")

    match opcao:
        case "1":
            for i in range(tamanho):
                usuario_existe = True

                while usuario_existe:
                    nomes_tentativa = input(f"Cadastre o nome do {i + 1}º usuário: ")

                    if nomes_tentativa not in nomes:
                        usuario_existe = False
                        nomes[i] = nomes_tentativa
                    else:
                        print("Esse nome de usuário já está cadastrado.")
                print("Requisitos de senha:\n - Maior ou igual a 8 caracteres; \n - Conter pelo menos 1 dos seguintes caracteres especiais: '!#$%&'()*+,-./:;<=>?@[\]^_`{|}~ ';")
                senha_tentativa1 = input(f"Cadastre a senha do {i + 1}º usuário: ")
                verifica = biblioteca.senhaValida(senha_tentativa1)
                while verifica == False:
                    senha_tentativa1 = input(f"Senha inválida! Verifique os requisitos de senha e tente novamente: ")
                    verifica = biblioteca.senhaValida(senha_tentativa1)

                senha_tentativa2 = input(f"Confirme a senha: ")

                if verifica == True:
                    while senha_tentativa1 != senha_tentativa2:
                        senha_tentativa2 = input(f"As senhas estão diferentes! Verifique e tente novamente: ")
                    senhas[i] = senha_tentativa1


                cpf[i] = input(f"Informe o CPF do {i + 1}º usuário (apenas números): ")
                print(f"O {i+1}º usuário  foi cadastrado com sucesso!")

        case "2":

            while tentativas > 0:
                nome_tentativa = input("Insira seu nome de usuário: ")

                if nome_tentativa in bloqueados:
                    print("Sua conta está bloqueada. Acesse o item 4 para desbloqueá-la.")
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

        case "3":
            print(nomes, senhas, cpf)
            print(bloqueados)
            for i in range(tamanho):
                print(f" Nome: {nomes[i]}, Senha: {senhas[i]}, CPF: {cpf[i]}, Posição: {i}")

        case "4":
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
                                print("Conta desbloqueada.")
                                restaura = True
                if restaura == False:
                    print("Informações incorretas. Tente novamente.")

        case "5":
            break
