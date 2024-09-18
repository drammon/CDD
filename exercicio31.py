while True:
    altura = float(input("Insira a altura: "))
    peso = float(input("Insira o peso: "))

    imc = (peso/(altura**2))

    if imc <= 18.5:
        print(f"Seu IMC é de {imc:.2f}, e você está abaixo do peso.")
    elif imc >= 18.6 and imc <= 24.9:
        print(f"Seu IMC é de {imc:.2f}, e você está no peso ideal, parabéns!")
    elif imc >= 25.0 and imc <= 29.9:
        print(f"Seu IMC é de {imc:.2f}, e você está levemente acima do peso.")
    elif imc >= 30.0 and imc <= 34.9:
        print(f"Seu IMC é de {imc:.2f}, e você está com Obesidade Grau I.")
    elif imc >= 35.0 and imc <= 39.9:
        print(f"Seu IMC é de {imc:.2f}, e você está com Obesidade Grau II (Severa).")
    elif imc >= 40.0:
        print(f"Seu IMC é de {imc:.2f}, e você está com Obesidade (Mórbida).")

    resp = int(input("Quer continuar? 1/sim e 2/não: "))
    if resp == 2:
        break

print("Obrigado.")
