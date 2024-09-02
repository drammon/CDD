litros = float(input("Digite a quantidade de combustível: "))
tipo = input("Digite 'G' para Gasolina ou 'E' para Etanol: ")

if tipo == "E" or tipo == "e" or tipo == "G" or tipo == "g":
    if tipo == "E" or tipo == "e":
        valor = litros * 4.90
    elif tipo == "G" or tipo == "g":
        valor = litros * 5.80

    print(f"O valor a ser pago é de {valor}.")

else:
    print("Tipo de combustível é inválido")

