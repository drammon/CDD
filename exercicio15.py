soma = 0
for i in range(10):
    num = int(input("Digite um número: "))
    if num % 2 != 0:
        soma += num
print(soma)