def piramide (num):
    for i in range(num+1):
        for x in range(i):
            print(i, end = " ")
        print()

def piramide2 (num):
    for i in range(num+1):
        for x in range(i):
            print(x, end = " ")
        print()

def contaVogais (txt):
    vogais = 0
    for i in txt:
        if i in "aeiou":
            vogais +=1
    print(vogais)
