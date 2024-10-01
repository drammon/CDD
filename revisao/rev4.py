#Faça um programa para ler o nome de uma pessoa, a sua idade e o seu salário e mostre essas informações na tela.

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
salario = float(input("Insira seu salário: "))

print(f"Olá, {nome}! Você tem {idade} anos e recebe R${salario} por mês.")