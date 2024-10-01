#Receba nome, duas notas e exiba a média do estudante.
nome = input("Digite seu nome: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2

print(f"A média de {nome} é: {media:.2}")

