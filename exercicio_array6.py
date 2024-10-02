nomes = ["", "", "", "", ""]
senhas = ["", "", "", "", ""]

for i in range(5):
    nomes[i] = input(f"Insira o nome do {i+1}º usuário: ")
    senhas[i] = input(f"Insira a senha do {i+1}º usuário: ")

for i in range(5):
    print(f" Nome: {nomes[i]}, Senha: {senhas[i]}, Posição: {i}")

