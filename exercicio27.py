while True:
    num = int(input("Insira um número: "))
    if num >= 0:
        if num % 2 == 0:
            print(f"{num} é par e positivo.")
        else:
            print(f"{num} é ímpar e positivo.")
    else:
        if num % 2 == 0:
            print(f"{num} é par e negativo.")
        else:
            print(f"{num} é ímpar e negativo.")

    repetir = int(input("Quer verificar outro número? 1/sim e 2/não: "))

    if repetir == 2:
        break

print("Fim.")