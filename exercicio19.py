resp = 0
while resp != 2:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    while num2 == 0:
        num2 = int(input("O número não pode ser 0, digite outro: "))

    divisao = num1/num2

    print(divisao)

    resp = int(input("Quer repetir a operação? Digite 1 para sim e 2 para não: "))
