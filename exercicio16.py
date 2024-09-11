quantidade_alunos = int(input("Quantos estudantes existem na sala? "))
soma_notas = 0

for i in range(quantidade_alunos):
    nota = float(input(f"Qual a nota do aluno nº {i+1}? "))
    soma_notas += nota

media = soma_notas / quantidade_alunos
print(f"{media:.2f}")