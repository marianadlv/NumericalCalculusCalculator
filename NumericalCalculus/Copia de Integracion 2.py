from sympy import *
import math
import cmath
import numpy as np

def solution():

    X = dict()
    fX = []

    numPuntos = eval(input("Número de puntos: "))

    for i in range(numPuntos):
        x = eval(input("x_" + str(i) + ": "))
        fx = eval(input("f(x_" + str(i) + "): "))
        X[x] = fx
        """X.append(eval(input("x_" + str(i) + ": ")))
        fX.append(eval(input("f(x_" + str(i) + "): ")))"""

    a = eval(input("a: "))
    b = eval(input("b: "))


#if numPuntos == 1:
   #trapecio
    numPuntos = 1

    h = (b - a) / (numPuntos)

    for i in range(numPuntos+1):
        fX.append(X[round(a+i*h,1)])

    res = (h/2)*(fX[0]+fX[1])

    print("Trapecio: ",res)

#elif numPuntos == 2:
    #Simpson
    numPuntos = 2
    h = (b - a) / (numPuntos)

    fX = []

    for i in range(numPuntos+1):
        fX.append(X[round(a+i*h,1)])

    res = (h/3)*(fX[0]+4*fX[1]+fX[2])

    print("Simpson: ", res)

#elif numPuntos == 3:
    #tres octavos
    numPuntos = 3
    h = (b - a) / (numPuntos)
    h = int(h *10) / 10             # truncar a un decimal

    fX = []

    for i in range(numPuntos + 1):
        fX.append(X[round(a + i * h, 1)])

    res = ((3*h)/8)*(fX[0]+3*fX[1]+3*fX[2]+fX[3])

    print("Tres octavos: ", res)

#elif numPuntos == 4:
    numPuntos = 4
    h = (b - a) / (numPuntos)

    fX = []

    for i in range(numPuntos + 1):
        fX.append(X[round(a + i * h, 1)])

    res = ((2 * h) / 45) * (7*fX[0] + 32 * fX[1] + 12 * fX[2] + 32*fX[3] + 7*fX[4])

    print("n = 4: ", res)

    #return "La integral en el intervalo [" + str(X[0]) + ", " + str(X[len(X)-1]) + "] es: " + str(res)

solution()
