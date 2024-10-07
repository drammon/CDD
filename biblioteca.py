

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
def senhaValida (senha_tentativa):

    caracteres_aceitos = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~ "
    caracteres_especiais = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~ "
    carac_invalidos = 0
    especiais_inseridos = 0

    senha_valida = False

    if len(senha_tentativa) >= 8:
        senha_valida = True

    for i in senha_tentativa:
        if i not in caracteres_aceitos:
            senha_valida = False
        elif i in caracteres_especiais:
            especiais_inseridos +=1

    if especiais_inseridos == 0:
        senha_valida = False

    return senha_valida






