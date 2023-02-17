# Developed by David Santiago Cruz Hernandez
import sys

LatinSquare = False
Group = False
Neutral = False
Inverse = False
Associativity = False


def start(matriz):
    print("Algotirmo desarrollado por David Santiago Cruz Hernandez, para Matematicas Discretas II")
    print()
    verifyLatinSquare(matriz)
    neutro = getNeutral(matriz, getSet(matriz))
    getInverse(matriz, getSet(matriz), neutro)
    checkAssociativity(matriz, getSet(matriz))
    printResults()


def getSet(matriz):
    set = matriz[0].copy()
    return set


def verifyLatinSquare(matriz):
    n = len(matriz)
    numRepetido = False
    for fila in range(n):
        listaRevisionFila = []
        listaRevisionCol = []
        for col in range(n):
            if matriz[fila][col] not in listaRevisionFila:
                listaRevisionFila.append(matriz[fila][col])
            else:
                numRepetido = True
                break

            if matriz[col][fila] not in listaRevisionCol:
                listaRevisionCol.append(matriz[col][fila])
            else:
                numRepetido = True
                break
        if numRepetido:
            break

    if not numRepetido:
        print("→ SI es un Cuadrado Latino\n")
        global LatinSquare
        LatinSquare = True


def getResult(matriz, a, b):
    fila = matriz[0].index(a)
    col = matriz[0].index(b)
    return matriz[fila][col]


def getNeutral(matriz, setG):
    neutro = ''
    for posibleNeutro in setG:
        contador = 0
        for dato in setG:
            if posibleNeutro == dato:
                continue
            resultado = getResult(matriz, posibleNeutro, dato)
            if dato == resultado:
                contador = contador + 1
                if contador == len(setG) - 1:
                    neutro = posibleNeutro
                    break

    if neutro != '':
        print("→ El Neutro es: " + neutro + "\n")
        global Neutral
        Neutral = True
    return neutro


def getInverse(matriz, setG, neutro):
    listaInversos = []
    for dato in setG:
        for posibleInverso in setG:
            resultado = getResult(matriz, posibleInverso, dato)
            if resultado == neutro:
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


def checkAssociativity(matriz, setG):
    listResults = []
    print("→ Asociaciones posibles:\n")
    for pos in range(len(setG) - 1):
        listResults.append(operateByPos(matriz, setG.copy(), pos))
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


def operateByPos(matriz, setG, pos):
    right = True
    for cont in range(len(setG) - 1):
        if not right:
            pos = pos - 1
        printAsssociativity(setG.copy(), pos)
        a = setG.pop(pos)
        b = setG.pop(pos)
        result = getResult(matriz, a, b)
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
    n = int(input("Ingrese el Tamaño n:"))
    matriz = []
    for size in range(n):
        matriz.append(input("Ingrese la Fila " + str(size) + " (separada por comas):").split(','))
    return matriz


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
    start(inputMatrix())
