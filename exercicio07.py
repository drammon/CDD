time1 = input("Digite o nome do time 1: ")
placar1 = int(input(f"Digite o placar do {time1}: "))

time2 = input("Digite o nome do time 2")
placar2 = int(input(f"Digite o placar do {time2}: "))

if placar1 > placar2:
    print(f"{time1} é o vencedor.")

elif placar1 == placar2:
    print("Empate!")

else:
    print(f"{time2} é o vencedor.")
