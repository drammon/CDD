#Faça um programa para calcular a média de 2 notas e mostrar essa média e o nome do aluno

nome = input("Insira seu nome: ")
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"{nome}, sua média foi {media}.")