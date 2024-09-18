while True:
    a = int(input("Insira o valor A: "))
    b = int(input("Insira o valor B: "))

    c = 0

    if a == b:
        c = a + b
    else:
        c = a*b
    print(c)

    repetir = int(input("Quer verificar outro número? 1/sim e 2/não: "))

    if repetir == 2:
        break
