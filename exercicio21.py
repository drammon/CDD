senha = "c_d_d:4.0"

tentativas = 5

while tentativas != 0:
    tentativa = input("Digite a sua senha : ")
    if tentativa == senha:
        print("Log-in realizado com sucesso!")
        break
    elif tentativa == "":
        print("Você precisa digitar algo.")
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Senha incorreta. Tente novamente, você tem mais {tentativas} tentativas: ")
        else:
            print("Senha incorreta. Acabaram suas chances.")


if tentativas == 0:
    print("Conta bloqueada.")


