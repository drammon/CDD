while True:
    a1 = float(input("Insira a primeira nota: "))
    while a1 < 0 or a1 > 10:
        a1 = float(input("Valor inválido, tente novamente: "))

    a2 = float(input("Insira a segunda nota: "))
    while a2 < 0 or a2 > 10:
        a2 = float(input("Valor inválido, tente novamente: "))

    media = (a1 + a2)/2
    print(media)

    repetir = input("Você deseja tentar de novo? s/n: ").lower()

    if repetir == "n":
        print("Ok, até a próxima!")
        break
