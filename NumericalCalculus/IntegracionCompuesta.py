from sympy import *
import math
import cmath
import numpy as np

"""def solution():

    opcion = eval(input("1. Cerradas \n2. Abiertas\n"))

    X = []
    fX = []

    if opcion == 1:

        def fun(x):
            return eval(f)

        op = eval(input("1. Función \n2. Puntos\n"))

        if op == 1:
            f = input("f(x): ")
            a = eval(input("a: "))
            b = eval(input("b: "))
            numPuntos = eval(input("n: "))

            h = (b - a) / numPuntos

            for i in range(numPuntos+1):
                X.append(a+i*h)
                fX.append(fun(X[i]))

        elif op == 2:
            numPuntos = eval(input("n: "))
            a = eval(input("a: "))
            b = eval(input("b: "))

            h = (b - a) / numPuntos

            for i in range(numPuntos+1):
                X.append(eval(input("x_" + str(i) + ": ")))
                fX.append(eval(input("f(x_" + str(i) + "): ")))

        #metodo = eval(input("1. Trapecio\n2. Simpson Compuesto\n"))

        metodo = 1

        if metodo == 1:             # trapecio

            res = 0

            res = res + fX[0] + fX[numPuntos]

            aux = 0

            for i in range(1, numPuntos):
                aux += fX[i]

            res += 2*aux

            res = res * (h/2)

            #return "La integral en el intervalo [" + str(a) + ", " + str(b) + "] es: " + str(res)
            sol = "La integral en el intervalo [" + str(a) + ", " + str(b) + "] es: " + str(res)
            print("Trapecio\n",sol)

        metodo = 2
        if metodo == 2:           # simpson                       SÓLO N PARES!!!!!

            res = 0

            res = res + fX[0] + fX[numPuntos]

            aux = 0

            for i in range(1,int((numPuntos/2)+1)):
                aux += 4*fX[(2*i)-1]

            res += aux

            aux = 0

            for i in range(1, int((numPuntos / 2))):
                aux += 2*fX[2*i]

            res += aux

            res = res * (h/3)

            #return "La integral en el intervalo [" + str(a) + ", " + str(b) + "] es: " + str(res)
            sol = "La integral en el intervalo [" + str(a) + ", " + str(b) + "] es: " + str(res)
            print("Simpson\n",sol)

            return

    elif opcion == 2:

        def fun(x):
            return eval(f)

        op = eval(input("1. Función \n2. Puntos\n"))

        if op == 1:
            f = input("f(x): ")
            a = eval(input("a: "))
            b = eval(input("b: "))
            numPuntos = eval(input("n: "))

            h = (b - a) / (numPuntos + 2)

            for i in range(numPuntos+1):
                X.append(a + (i+1)*h)
                fX.append(fun(X[i]))

        elif op == 2:
            a = eval(input("a: "))
            b = eval(input("b: "))
            numPuntos = eval(input("n: "))

            for i in range(numPuntos+1):
                X.append(eval(input("x_" + str(i) + ": ")))
                fX.append(eval(input("f(x_" + str(i) + "): ")))

        res = 0

        for i in range(0, int((numPuntos / 2) + 1)):
            res += fX[2 * i]

        res = res * (2 * h)

        return "La integral en el intervalo [" + str(a) + ", " + str(b) + "] es: " + str(res)

print(solution())"""

class IntegracionCompuesta:

    def __init__(self, opcion, f, n, fX, a, b, op=0):
        self.opcion = eval(opcion)
        # 1 Cerrada
        # 2 Abierta
        self.f = f
        if f != "":
            self.op = 1
        else:
            self.op = 0
        self.n = eval(n)
        if fX[0] != '':
            self.fX = []
            for num in fX:
                self.fX.append(eval(num))
        else:
            self.fX = ""
        self.a = eval(a)
        self.b = eval(b)

    def solution(self):

        if self.opcion == 0:     # Trapecio

            def fun(x):
                return eval(self.f)

            op = self.op

            if op == 1:
                a = self.a
                b = self.b
                numPuntos = self.n

                h = (b - a) / numPuntos

                X = []
                fX = []

                for i in range(numPuntos + 1):
                    X.append(a + i * h)
                    fX.append(fun(X[i]))

                res = 0

                res = res + fX[0] + fX[numPuntos]

                aux = 0

                for i in range(1, numPuntos):
                    aux += fX[i]

                res += 2 * aux

                res = res * (h / 2)

                return "La integral en el intervalo [" + str(a) + ", " + str(b) + "] es: " + str(res)

            else:

                a = self.a
                b = self.b
                numPuntos = self.n
                fX = self.fX

                h = (b - a) / numPuntos

                res = 0

                res = res + fX[0] + fX[numPuntos]

                aux = 0

                for i in range(1, numPuntos):
                    aux += fX[i]

                res += 2 * aux

                res = res * (h / 2)

                return "La integral en el intervalo [" + str(a) + ", " + str(b) + "] es: " + str(res)

        elif self.opcion == 1:     # Simpson

            def fun(x):
                return eval(self.f)

            op = self.op

            if op == 1:
                a = self.a
                b = self.b
                numPuntos = self.n

                h = (b - a) / numPuntos

                X = []
                fX = []

                for i in range(numPuntos + 1):
                    X.append(a + i * h)
                    fX.append(fun(X[i]))

                res = 0

                res = res + fX[0] + fX[numPuntos]

                aux = 0

                for i in range(1, int((numPuntos / 2) + 1)):
                    aux += 4 * fX[(2 * i) - 1]

                res += aux

                aux = 0

                for i in range(1, int((numPuntos / 2))):
                    aux += 2 * fX[2 * i]

                res += aux

                res = res * (h / 3)

                return "La integral en el intervalo [" + str(a) + ", " + str(b) + "] es: " + str(res)

            else:

                a = self.a
                b = self.b
                numPuntos = self.n
                fX = self.fX

                h = (b - a) / numPuntos

                res = 0

                res = res + fX[0] + fX[numPuntos]

                aux = 0

                for i in range(1, int((numPuntos / 2) + 1)):
                    aux += 4 * fX[(2 * i) - 1]

                res += aux

                aux = 0

                for i in range(1, int((numPuntos / 2))):
                    aux += 2 * fX[2 * i]

                res += aux

                res = res * (h / 3)

                return "La integral en el intervalo [" + str(a) + ", " + str(b) + "] es: " + str(res)

        elif self.opcion == 2:   # Abierta

            def fun(x):
                return eval(self.f)

            if self.op == 1:

                numPuntos = self.n
                a = self.a
                b = self.b

                h = (b - a) / (numPuntos + 2)

                X = []
                fX = []

                for i in range(numPuntos + 1):
                    X.append(a + (i + 1) * h)
                    fX.append(fun(X[i]))

                res = 0

                for i in range(0, int((numPuntos / 2) + 1)):
                    res += fX[2 * i]

                res = res * (2 * h)

                return "La integral en el intervalo [" + str(self.a) + ", " + str(self.b) + "] es: " + str(res)

            else:
                res = 0
                numPuntos = self.n
                h = (self.b-self.a)/(numPuntos+2)

                for i in range(0, int((numPuntos / 2) + 1)):
                    res += self.fX[2 * i]

                res = res * (2 * h)

                return "La integral en el intervalo [" + str(self.a) + ", " + str(self.b) + "] es: " + str(res)
