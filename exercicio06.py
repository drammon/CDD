#Receba três notas e exiba se o aluno foi aprovado, reprovado ou está em recuperação

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3)/3

if media >= 7.0:
    print("Aluno aprovado.")
elif 7 > media > 4:
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado.")

