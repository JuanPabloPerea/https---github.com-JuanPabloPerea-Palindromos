a = "Anita lava la tina"
c = "AABBsopAsAposCCDD"
d = "123456 6 54321"


def palindromo(cadena):
    cadena2 = cadena.lower()
    aux = []
    aux2 = []
    for i in cadena2:
        if (i != " "):
            aux.append(i)
    print(aux)
    for j in reversed(cadena2):
        if (j != " "):
            aux2.append(j)
    if (aux == aux2):
        return True
    else:
        return False


def subPalindromo(cadena):
    aux2 = ""
    aux = ""
    cont = 0
    rep = 1
    for i in cadena:
        cont += 1
        num = cont
        for j in cadena[cont:]:
            num += 1
            if (i == j):
                rep += 1
                aux = cadena[cont-1:num]
                if (palindromo(aux) == False):
                    aux = ""
                    rep -= 1
                else:
                    if (len(aux) > len(aux2)):
                        aux2 = aux
    return (aux2)


print(subPalindromo(d))
