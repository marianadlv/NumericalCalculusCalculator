from sympy import *
import math
import cmath
import numpy as np

def solution():

    #opcion = eval(input("1. Cerradas \n2. Abiertas\n"))

    X = []
    fX = []

    #if opcion == 1:

    def fun(x):
        return eval(f)

    #op = eval(input("1. Función \n2. Puntos\n"))

    cont = 0
    res = [0]*8

    while cont < 2:


        #if op == 1:
        f = input("f(x): ")
        a = eval(input("a: "))
        b = eval(input("b: "))
        #numPuntos = eval(input("n: "))

        """X.append(a)
        fX.append(fun(a))
    
        for i in range(1,numPuntos):
            X.append(X[i-1]+h)
            fX.append(fun(X[i]))
    
        X.append(b)
        fX.append(fun(b))"""

        """elif op == 2:
            numPuntos = eval(input("n: "))
    
            for i in range(numPuntos+1):
                X.append(eval(input("x_" + str(i) + ": ")))
                fX.append(eval(input("f(x_" + str(i) + "): ")))
    
            h = X[1] - X[0]"""

    #if numPuntos == 1:
       #trapecio
        numPuntos = 1
        h = (b - a) / (numPuntos)

        X = []
        fX = []

        X.append(a)
        fX.append(fun(a))

        for i in range(1, numPuntos):
            fX.append(fun(X[i]))

        X.append(b)
        fX.append(fun(b))

        res[0] += (h/2)*(fX[0]+fX[1])


    #elif numPuntos == 2:
        #Simpson
        numPuntos = 2
        h = (b - a) / (numPuntos)

        X = []
        fX = []

        X.append(a)
        fX.append(fun(a))

        for i in range(1, numPuntos):
            X.append(X[i - 1] + h)
            fX.append(fun(X[i]))

        X.append(b)
        fX.append(fun(b))
        res[1] += (h/3)*(fX[0]+4*fX[1]+fX[2])

    #elif numPuntos == 3:
        #tres octavos
        numPuntos = 3
        h = (b - a) / (numPuntos)

        X = []
        fX = []

        X.append(a)
        fX.append(fun(a))

        for i in range(1, numPuntos):
            X.append(X[i - 1] + h)
            fX.append(fun(X[i]))

        X.append(b)
        fX.append(fun(b))
        res[2] += ((3*h)/8)*(fX[0]+3*fX[1]+3*fX[2]+fX[3])

    #elif numPuntos == 4:
        numPuntos = 4
        h = (b - a) / (numPuntos)

        X = []
        fX = []

        X.append(a)
        fX.append(fun(a))

        for i in range(1, numPuntos):
            X.append(X[i - 1] + h)
            fX.append(fun(X[i]))

        X.append(b)
        fX.append(fun(b))
        res[3] += ((2 * h) / 45) * (7*fX[0] + 32 * fX[1] + 12 * fX[2] + 32*fX[3] + 7*fX[4])


        #return "La integral en el intervalo [" + str(X[0]) + ", " + str(X[len(X)-1]) + "] es: " + str(res)

        #elif opcion == 2:

        #n = eval(input("n: "))

        #if n == 0:

        numPuntos = 0

        h = (b-a)/(numPuntos+2)
        x = a + h

        res[4] += 2*h*fun(x)



            #return "La integral en el intervalo [" + str(a) + ", " + str(b) + "] es: " + str(res)

        """else:
    
            for i in range(n+1):
                X.append(eval(input("x_" + str(i) + ": ")))
                fX.append(eval(input("f(x_" + str(i) + "): ")))
    
            h = X[1] - X[0]"""

    #if n == 1:

        numPuntos = 1
        h = (b - a) / (numPuntos+2)

        X = []
        fX = []

        """X.append(a)
        fX.append(fun(a))
    
        for i in range(1, numPuntos):
            X.append(X[i - 1] + h)
            fX.append(fun(X[i]))
    
        X.append(b)
        fX.append(fun(b))"""

        for i in range(1,numPuntos+2):
            X.append(a + i*h)
            fX.append(fun(X[i-1]))

        res[5] += ((3*h)/2)*(fX[0]+fX[1])



    #elif n == 2:

        numPuntos = 2
        h = (b - a) / (numPuntos+2)

        X = []
        fX = []

        for i in range(1, numPuntos + 2):
            X.append(a + i * h)
            fX.append(fun(X[i - 1]))

        res[6] += ((4*h)/3)*(2*fX[0]-fX[1]+2*fX[2])



        #elif n == 3:

        numPuntos = 3
        h = (b - a) / (numPuntos+2)

        X = []
        fX = []

        for i in range(1, numPuntos + 2):
            X.append(a + i * h)
            fX.append(fun(X[i - 1]))

        res[7] += ((5*h)/24)*(11*fX[0]+fX[1]+fX[2]+11*fX[3])



        #return "La integral en el intervalo [" + str(X[0]) + ", " + str(X[len(X)-1]) + "] es: " + str(res)

        cont += 1

    print("Cerradas: \nTrapecio: ", res[0])
    print("Simpson: ", res[1])
    print("Tres octavos: ", res[2])
    print("n = 4: ", res[3])
    print("Abiertas: \nn=0: ", res[4])
    print("n=1: ", res[5])
    print("n=2: ", res[6])
    print("n=3: ", res[7])


solution()
