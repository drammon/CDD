hora1 = [int(i) for i in input("Digite o primeiro horário: ").split(":")]
hora2 = [int(i) for i in input("Digite o horário de saída: ").split(":")]

if hora1[0] > 12:
    hora1[0] -= 12

if hora2[0] > 12:
    hora2[0] -= 12

totalH = hora1[0] + hora2[0]
totalMin = hora1[1] + hora2[1]
if totalH > 12:
    totalH -= 12
if totalMin >= 60:
    totalMin = totalMin - 60
    totalH += 1

print(f"{totalH}:{totalMin:02d}")
