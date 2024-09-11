num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

while num2 == 0:
    num = int(input("O número não pode ser 0, digite outro: "))
    num2 = num

divisao = num1/num2

print(divisao)

