total = 0
qt = 0
while qt < 10:
    num = int(input(f"Digite o {qt+1}º número: "))
    qt += 1
    total += num

media = total/qt
print(media)

