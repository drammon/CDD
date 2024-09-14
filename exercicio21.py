senha = "c_d_d:4.0"

tentativas = 3
while tentativas != 0:
    tentativa = input("Digite a sua senha : ")
    if tentativa == senha:
        print("Log-in realizado com sucesso!")
        break
    elif tentativa == "":
        print("Você precisa digitar algo.")
    elif tentativas == 0:
        print("Senha incorreta. A conta será bloqueada.")
    else:
        tentativas -= 1
        print(f"Senha incorreta. Tente novamente, você tem mais {tentativas} tentativas: ")


if tentativas == 0:
    print("Conta bloqueada.")


