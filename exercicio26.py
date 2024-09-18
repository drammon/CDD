repetir = 0

while repetir != 2:
    a = int(input("Insira o valor A: "))
    b = int(input("Insira o valor B: "))
    c = int(input("Insira o valor C: "))
    soma = a + b
    if soma > c:
        print(f"A soma dá {soma}, logo, é maior que C.")
    elif soma == c:
        print(f"A soma dá {soma}, logo, é igual a C.")
    else:
        print(f"A soma dá {soma}, logo, é menor que C.")

    repetir = int(input("Quer verificar outros números? 1/sim e 2/não: "))

print("Fim")