notas = ["", "", "", "", ""]

for i in range(len(notas)):
    notas[i] = float(input(f"Digite a {i+1}º nota: "))
somaNotas = 0
for i in range(len(notas)):
    somaNotas += notas[i]

media = somaNotas/len(notas)

acimaMedia = 0

for i in range(len(notas)):
    if notas[i] > media:
        acimaMedia += 1
        
print(f"A média da turma é {media:.2f}. {acimaMedia} estudantes ficaram acima da média.")
