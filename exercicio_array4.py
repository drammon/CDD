x = int(input("Digite um valor para multiplicar os números: "))
a = ["", "", "", "", "", "", "", "", "", ""]
m = ["", "", "", "", "", "", "", "", "", ""]

for i in range(len(a)):
    num =  int(input(f"Digite o {i+1}º número: "))
    a[i] = num

for i in range(len(a)):
    m[i] = a[i] * x

print(a)
print(x)
print(m)

