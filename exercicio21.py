pin = "c_d_d:4.0"

tentativas = 3

while tentativas != 0:
    senha = input("Digite a sua senha : ")
    if senha == pin:
        print("Log-in realizado com sucesso!")
        break
    elif senha == "":
        print("Você precisa digitar algo.")
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Senha incorreta. Tente novamente, você tem mais {tentativas} tentativas: ")
        else:
            print("Senha incorreta. Acabaram suas chances.")


if tentativas == 0:
    print("Conta bloqueada.")


