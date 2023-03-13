# Developed by David Santiago Cruz Hernandez

Matrix = []
Border = []
LatinSquare = False
Group = False
Neutral = False
NeutralResult = 0
Inverse = False
Associativity = False


def start():
    print("Algotirmo desarrollado por David Santiago Cruz Hernandez, para Matematicas Discretas II")
    inputMatrix()
    verifyLatinSquare()
    getNeutral(getSet())
    getInverse(getSet())
    checkAssociativity(getSet())
    printResults()


def getSet():
    set = Matrix[0].copy()
    return set


def verifyLatinSquare():
    n = len(Matrix)
    numRepetido = False
    for fila in range(n):
        listaRevisionFila = []
        listaRevisionCol = []
        for col in range(n):
            if Matrix[fila][col] not in listaRevisionFila:
                listaRevisionFila.append(Matrix[fila][col])
            else:
                numRepetido = True
                break

            if Matrix[col][fila] not in listaRevisionCol:
                listaRevisionCol.append(Matrix[col][fila])
            else:
                numRepetido = True
                break
        if numRepetido:
            break

    if not numRepetido:
        print("→ SI es un Cuadrado Latino\n")
        global LatinSquare
        LatinSquare = True


def getResult(a, b):
    fila = Border.index(a)
    col = Border.index(b)
    return Matrix[fila][col]


def getNeutral(setG):
    global NeutralResult
    for posibleNeutro in setG:
        contador = 0
        for dato in setG:
            resultado = getResult(posibleNeutro, dato)
            if dato == resultado:
                contador = contador + 1
                if contador == len(setG):
                    NeutralResult = posibleNeutro
                    break
            else:
                break

    if NeutralResult != "":
        print("→ El Neutro es: " + NeutralResult + "\n")
        global Neutral

        Neutral = True


def getInverse(setG):
    listaInversos = []
    for dato in setG:
        for posibleInverso in setG:
            resultado = getResult(posibleInverso, dato)
            if resultado == NeutralResult:
                if posibleInverso not in listaInversos:
                    listaInversos.append(posibleInverso)
                    continue
                else:
                    break
    if len(listaInversos) == len(setG):
        for pos in range(len(setG)):
            print("→ El inverso de " + setG[pos] + " es: " + listaInversos[pos])
        print()
        global Inverse
        Inverse = True
    else:
        print("→ No hay un Inverso para cada elemento del conjunto.\n")


def checkAssociativity(setG):
    listResults = []
    print("→ Asociaciones posibles:\n")
    for pos in range(len(setG) - 1):
        listResults.append(operateByPos(setG.copy(), pos))
        print()

    print("→ Resultados de la Asociatividad obtenidos: " + str(listResults))
    asssociativity = True
    for dato in listResults:
        if listResults[0] != dato:
            asssociativity = False
            break
    if asssociativity:
        print(" El conjunto SI es asociativo\n")
        global Associativity
        Associativity = True
    else:
        print(" El conjunto NO es asociativo\n")


def operateByPos(setG, pos):
    right = True
    for cont in range(len(setG) - 1):
        if not right:
            pos = pos - 1
        printAsssociativity(setG.copy(), pos)
        a = setG.pop(pos)
        b = setG.pop(pos)
        result = getResult(a, b)
        setG.insert(pos, result)

        if right:
            try:
                setG[pos + 1]
            except IndexError:
                right = False
    print(setG[0])
    return setG[0]


def printAsssociativity(setG, pos):
    operation = ""
    for times in range(pos):
        operation = operation + setG[times] + "•"
    operation = operation + "(" + setG[pos] + "•" + setG[pos + 1] + ")"
    for times in range(pos + 2, len(setG)):
        operation = operation + "•" + setG[times]
    print(operation)


def inputMatrix():
    while True:
        n = int(input("Ingrese el Tamaño n:"))
        global Border
        Border = input("Ingrese los elementos del Marco de la Tabla (separados por comas):  ").split(',')
        for size in range(n):
            Matrix.append(input("Ingrese la Fila " + str(size) + " (separada por comas):").split(','))
        if verifyInput():
            break
        else:
            print("\n ---- Por favor ingrese una tabla valida!! ---- \n")


def verifyInput():
    for subList in Matrix:
        for element in subList:
            if element not in Border:
                return False
    return True


def printResults():
    print(" --------------- Resultados Obtenidos --------------- \n")

    print("→ Cuadrado Latino: " + returnIcon(LatinSquare))
    print()

    print("→ Existe un Elemento Neutro: " + returnIcon(Neutral))

    print("→ Existe un Inverso para cada elemento del Conjunto: " + returnIcon(Inverse))

    print("→ Es Asociativo: " + returnIcon(Associativity))

    Answer = lambda: f"SI" if (Neutral and Inverse and Associativity) else f"NO"
    print(" ---- Por lo tanto, " + Answer() + " es un Grupo." + "\n")


def returnIcon(answer):
    if answer:
        return "✅"
    else:
        return "❌"


if __name__ == '__main__':
    start()
