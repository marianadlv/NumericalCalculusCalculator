from sympy import *
import math
import cmath
import numpy as np

def solution():

    opcion = eval(input("Escriba el número de la opción deseada: \n0. Diferencia progresiva y regresiva \n1. Extremo de 3 puntos \n2. Intermedio de 3 puntos \n3. Extremo de 5 puntos \n4. Intermedio de 5 puntos\n"))

    X = []
    fX = []

    if opcion == 0:

        X.append(eval(input("x_0: ")))
        fX.append(eval(input("f(x_0): ")))
        X.append(eval(input("x_1: ")))
        fX.append(eval(input("f(x_1): ")))
        h = X[1] - X[0]

        dif1 = (fX[1]-fX[0]) / h
        #return dif1
        return "La primera derivada evaluada en " + str(X[0]) + " es: " + str(dif1)


    elif opcion == 1:
        n = 3
        for i in range(n):
            X.append(eval(input("x_"+str(i)+": ")))
            fX.append(eval(input("f(x_"+str(i)+"): ")))
        h = X[1] - X[0]

        dif1 = (1/(2*h)) * (-3*fX[0]+4*fX[1]-fX[2])

        return "La primera derivada evaluada en " + str(X[0]) + " es: " + str(dif1)
        #return dif1

    elif opcion == 2:
        n = 3
        X = [0]*n
        fX = [0] * n
        X[1] = eval(input("x_0: "))
        fX[1] = eval(input("f(x_0): "))
        X[0] = eval(input("x_1: "))
        fX[0] = eval(input("f(x_1): "))
        X[2] = eval(input("x_2: "))
        fX[2] = eval(input("f(x_2): "))
        h = X[2] - X[1]

        dif1 = (1/(2*h)) * (fX[2]-fX[0])
        #dif2 = (1/(h**2)) * (fX[0] - 2*fX[1] + fX[2])

        return "La primera derivada evaluada en " + str(X[1]) + " es: " + str(dif1)
        #return dif1
    #"\nLa segunda derivada evaluada en " + str(X[1]) + " es: " + str(dif2)



    elif opcion == 3:
        n = 5
        for i in range(n):
            X.append(eval(input("x_"+str(i)+": ")))
            fX.append(eval(input("f(x_"+str(i)+"): ")))
        h = X[1] - X[0]

        dif1 = (1/(12*h)) * ( -25*fX[0] + 48*fX[1] - 36*fX[2] + 16*fX[3] - 3*fX[4] )

        return "La primera derivada evaluada en " + str(X[0]) + " es: " + str(dif1)
        #return dif1


    elif opcion == 4:
        n = 5
        X = [0] * n
        fX = [0] * n
        X[2] = eval(input("x_0: "))
        fX[2] = eval(input("f(x_0): "))
        X[0] = eval(input("x_1: "))
        fX[0] = eval(input("f(x_1): "))
        X[1] = eval(input("x_2: "))
        fX[1] = eval(input("f(x_2): "))
        X[3] = eval(input("x_3: "))
        fX[3] = eval(input("f(x_3): "))
        X[4] = eval(input("x_4: "))
        fX[4] = eval(input("f(x_4): "))
        h = X[4] - X[3]

        dif1 = (1/(12*h)) * ( fX[0] - 8*fX[1] + 8*fX[3] - fX[4] )

        return "La primera derivada evaluada en " + str(X[2]) + " es: " + str(dif1)
        #return dif1

    elif opcion == 5:
        n = 5
        X = [0] * n
        fX = [0] * n
        X[0] = eval(input("x_0: "))
        fX[0] = eval(input("f(x_0): "))
        X[1] = eval(input("x_1: "))
        fX[1] = eval(input("f(x_1): "))
        X[2] = eval(input("x_2: "))
        fX[2] = eval(input("f(x_2): "))
        X[3] = eval(input("x_3: "))
        fX[3] = eval(input("f(x_3): "))
        X[4] = eval(input("x_4: "))
        fX[4] = eval(input("f(x_4): "))
        h = -1*(X[1]-X[0])

        dif1 = (-5/(6*h))*fX[0] - (1/(4*h))*fX[1] + (3/(2*h))*fX[2] - (1/(2*h))*fX[3] + (1/(12*h))*fX[4]

        return "La primera derivada evaluada en " + str(X[2]) + " es: " + str(dif1)

        #return dif1


dif = solution()

print(dif)
