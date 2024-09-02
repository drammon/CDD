litros = float(input("Digite a quantidade de combustível: "))
tipo = input("")

if tipo == "E" and tipo == "e":
    valor = litros * 4.90
    print(f"O valor a ser pago é de {valor}.")
else:
    valor = litros * 5.80
    print(f"O valor a ser pago é de {valor}.")