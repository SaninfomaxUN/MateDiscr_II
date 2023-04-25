#!/usr/bin/env python
# coding: utf-8

# <h1>Taller #2: Cálculo del número de generadores del Grupo Cíclico de G</h1>

# <h4> Presentado por: David Santiago Cruz Hernandez</h4>
# <h4> Asignatura: Matemáticas Discretas II </h4>

# In[ ]:


import time
numGeneradoresGCiclico = 0
dicDescomposicionPrimosGrupo = {}


# In[ ]:


def bold(texto):
    return "\033[1m" + texto + "\033[0m"


# In[ ]:


def imprimirSuperIndice(indice):
    if indice == 1:
        return str(chr(0x00b9))
    elif 2 <= indice <= 3:
        return str(chr(0x00b0 + indice))
    else:
        return str(chr(0x2070 + indice))


# In[ ]:


n = int(input("Ingrese el Orden de G:"))


# In[ ]:


Grupo = []
for num in range(1,n+1):
    Grupo.append(num)


# ### Metodo Alternativo:
# ##### Comprobación por medio del siguiente *Lema*:

# ###### • **i)** φ(I) = 1
# ###### • **ii)** Si *p* es **primo**, entonces el **φ($p^{a}$) =** $p^{a}$ - $p^{a-1}$
# ###### • **iii)** Si *mcd(m,n)* = 1, entonces el **φ(m•n) =** φ(m) + φ(n)

# In[ ]:


def calcularDescomposicionPrimos(resultadoDivision,dicDescomposicionPrimos):
    potencia = 1
    for divisor in range(2,len(Grupo)):
        while resultadoDivision%divisor==0:
            resultadoDivision = resultadoDivision/divisor
            if divisor not in dicDescomposicionPrimos:
                potencia = 1
            dicDescomposicionPrimos[divisor] = potencia
            potencia+=1
        if resultadoDivision ==1:
            break
    return dicDescomposicionPrimos


# In[ ]:


def LemaTotientEulerPrimos():
    resultado = 1
    for primo in dicDescomposicionPrimosGrupo:
        indice = dicDescomposicionPrimosGrupo.get(primo)
        resultado = resultado * (pow(primo,indice) - pow(primo,indice-1))
    return resultado


# In[ ]:


inicio2 = time.time()
dicDescomposicionPrimosGrupo = calcularDescomposicionPrimos(len(Grupo), {})
numGeneradoresGCiclico = LemaTotientEulerPrimos()

fin2 = time.time()
Tiempo2 = round(fin2-inicio2,4)


# In[ ]:


def imprimirCadenaDescomposicion():
    strDescomposicion = ""
    for base in dicDescomposicionPrimosGrupo:
        strIndice = imprimirSuperIndice(dicDescomposicionPrimosGrupo[base])
        strDescomposicion = strDescomposicion + str(base) + strIndice + "•"
    return strDescomposicion[0:-1]


# In[ ]:


def imprimirCadenaDescomposicionTotient():
    strLemaIII = ""
    for potencia in imprimirCadenaDescomposicion().split("•"):
        strLemaIII = strLemaIII + "φ(" + potencia + ")•"

    strLemaII = ""
    for base in dicDescomposicionPrimosGrupo:
        strLemaII = strLemaII + "(" + str(base) + imprimirSuperIndice(dicDescomposicionPrimosGrupo[base]) + "-" + str(base) + imprimirSuperIndice(dicDescomposicionPrimosGrupo[base] - 1) + ")•"
    return strLemaIII[0:-1] + " = " + strLemaII[0:-1]


# In[ ]:


print("                    " + bold("Orden del Grupo G: " + str(n)) + "\n")
print("Tiempo de ejecución del Metodo Alternativo: " + str(Tiempo2) + " segundos.")
print("→ Descomposición de Factores Primos de " + bold("n") + ": " + imprimirCadenaDescomposicion())
print(bold("→ Número de Generadores Cíclicos de G:"))
print("      φ(" + str(n) + ") = φ(" + imprimirCadenaDescomposicion() + ") = " + imprimirCadenaDescomposicionTotient() + " = " + str(numGeneradoresGCiclico) )
print("→ Por este Metodo, no se obtiene la lista de los Generadores Cíclicos de G.")


# ### Metodo Tradicional:
# ##### Comprobar si el subgrupo generado por cada elemento es el Grupo Cíclico de G.

# In[ ]:


def calcularMCDconGrupo(numGenerador):
    listaPrimosComunes = []
    mcd = 1
    descPrimosNumGenerador = calcularDescomposicionPrimos(numGenerador, {})
    menorRepeticion = lambda x, y: x if x <= y else y
    for primo in descPrimosNumGenerador:
        if primo in dicDescomposicionPrimosGrupo:
            listaPrimosComunes.append(
                pow(primo, menorRepeticion(descPrimosNumGenerador[primo], dicDescomposicionPrimosGrupo[primo])) )
    for primo in listaPrimosComunes:
        mcd = mcd * primo
    return mcd


# In[ ]:


###### Se calcula cada subgrupo generado por cada elemento (y se almacena en un Set). Luego, se comprueba su tamaño:


# In[ ]:


def generador(numGenerador):
    SubGrupo = set()
    strIndice = ""
    for indice in Grupo:
        SubGrupo.add(indice * numGenerador % n)
        if indice * numGenerador % n == 0:
            break
    for digit in str(numGenerador):
        strIndice = strIndice + imprimirSuperIndice(int(digit))
    if len(SubGrupo) == len(Grupo):
        print("< a" + strIndice + "> = " + bold("--- Grupo Cíclico de G ---"))
        return True
    else:
        mcd = calcularMCDconGrupo(numGenerador)
        if mcd == numGenerador or mcd == 1:
            print("< a" + strIndice + "> = ", end="")
            print(SubGrupo)
        else:
            print("< a" + strIndice + "> = " + "Subgrupo Cíclico generado por " + str(mcd))

        return False


# In[ ]:


GeneradoresGCiclico = []
numGeneradoresGCiclico=0
inicio1 = time.time()

for num in Grupo:
    if generador(num):
        numGeneradoresGCiclico+=1
        GeneradoresGCiclico.append(num)

fin1 = time.time()
Tiempo1 = round(fin1-inicio1,2)


# In[ ]:


print("                                   " + bold("Orden del Grupo G: " + str(n)) + "\n")
print(bold("→ Generadores Cíclicos de G:"))
print(bold("|") + " { " + ', '.join(str(x) for x in GeneradoresGCiclico) + " } " + bold("|" + " = " + str(numGeneradoresGCiclico))+ "\n")

print("Tiempo de ejecución del " + bold("Metodo Tradicional") + ": " + str(Tiempo1) + " segundos.")
print(bold("→ Número de Generadores Cíclicos de G: --- φ(" + str(n) + ") = " + str(numGeneradoresGCiclico) + " ---"))


# In[ ]:


##### Muchas Gracias. Desarrollado por David Santiago Cruz Hernandez. Correo: dcruzhe@unal.edu.co

