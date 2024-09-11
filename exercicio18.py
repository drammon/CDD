qtAlunos = int(input("Quantos alunos tem na sala? "))
total = 0
cont = 0
while cont < qtAlunos:
    num = int(input(f"Digite o {cont+1}º número: "))
    cont += 1
    total += num

media = total/qtAlunos
print(media)

