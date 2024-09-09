hora1 = [int(i) for i in input("Digite o primeiro horário: ").split(":")]
hora2 = [int(i) for i in input("Digite o segundo horário: ").split(":")]

if hora1[0] > 12:
    hora1[0] -= 12

if hora2[0] > 12:
    hora2[0] -= 12

totalHr = hora1[0] + hora2[0]
totalMin = hora1[1] + hora2[1]

if totalMin >= 60:
    totalMin -= 60
    totalHr += 1

if totalHr > 12:
    totalHr -= 12

if totalMin < 10:
    print(f"{totalHr}:0{totalMin}")
else:
    print(f"{totalHr}:{totalMin}")
