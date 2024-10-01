#Receba a quantidade de combustível, assim como o tipo, e exiba o valor:
litros = float(input("Digite a quantidade de combustível: "))
tipo = input("Digite 'G' para Gasolina ou 'E' para Etanol: ")

if tipo == "E" or tipo == "e" or tipo == "G" or tipo == "g":
    if tipo == "E" or tipo == "e":
        #valor do etanol: 4.90
        valor = litros * 4.90
    elif tipo == "G" or tipo == "g":
        # valor da gasolina: 5.80
        valor = litros * 5.80

    print(f"O valor a ser pago é de {valor}.")

else:
    print("Tipo de combustível é inválido")

