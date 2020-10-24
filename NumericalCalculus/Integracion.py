from sympy import *
import math
import cmath
import numpy as np

#if self.numPuntos != len(self.X) or self.numPuntos != len(self.fX): return "Número incorrecto de puntos."

class Integracion:

    def __init__(self,opcion,f,n,X,fX,a,b,op=0):
        # f para abierta y cerrada
        # n para abierta
        # n2 para cerrada
        # X y fX para abierta y cerrada
        # a y b para abierta y cerrada
        self.opcion = eval(opcion)
        self.f = f
        if f != "":
           self.op = 1
        else:
            self.op = 0
        self.n = eval(n)
        if X[0] != '':
            self.X = []
            for num in X:
                self.X.append(eval(num))
        else:
            self.X = ""
        if fX[0] != '':
            self.fX = []
            for num in fX:
                self.fX.append(eval(num))
        else:
            self.fX = ""
        self.a = eval(a)
        self.b = eval(b)

    def solution(self):

        opcion = self.opcion

        X = self.X
        fX = self.fX

        if opcion == 1:         # Abierta

            def fun(x):
                return eval(self.f)

            if self.op == 1:
                f = self.f
                a = self.a
                b = self.b
                numPuntos = self.n
                X = []
                fX = []

                h = (b - a) / (numPuntos)

                X.append(a)
                fX.append(fun(a))

                for i in range(1,numPuntos+1):
                    X.append(X[i-1]+h)
                    fX.append(fun(X[i]))

                X.append(b)
                fX.append(fun(b))

            numPuntos = self.n
            b = self.b
            a = self.a

            if numPuntos == 1:
               #trapecio
                h = (b - a) / (numPuntos)

                res = (h/2)*(fX[0]+fX[1])

                #return "Trapecio: " + str(res)

            elif numPuntos == 2:
                #Simpson
                h = (b - a) / (numPuntos)

                res = (h/3)*(fX[0]+4*fX[1]+fX[2])
                #return "Simpson: " + str(res)

            elif numPuntos == 3:
                #tres octavos
                h = (b - a) / (numPuntos)

                res = ((3*h)/8)*(fX[0]+3*fX[1]+3*fX[2]+fX[3])

                #return "Tres octavos: " + str(res)

            elif numPuntos == 4:
                h = (b - a) / (numPuntos)

                res = ((2 * h) / 45) * (7*fX[0] + 32 * fX[1] + 12 * fX[2] + 32*fX[3] + 7*fX[4])

                #return "n = 4: " + str(res)

            return "La integral en el intervalo [" + str(X[0]) + ", " + str(X[len(X)-1]) + "] es: " + str(res)

        elif self.opcion == 2:      # Cerrada

            n = self.n
            op = self.op

            if n == 0 or op == 1:

                def fun(x):
                    return eval(self.f)

                a = self.a
                b = self.b
                h = (b-a)/2
                x = a + h
                res = 2*h*fun(x)

                #print("n=0: ",res)

                return "La integral en el intervalo [" + str(a) + ", " + str(b) + "] es: " + str(res)

            else:

                X = self.X
                fX = self.fX

                h = X[1] - X[0]

                if n == 1:
                    res = ((3*h)/2)*(fX[0]+fX[1])

                elif n == 2:
                    res = ((4*h)/3)*(2*fX[0]-fX[1]+2*fX[2])

                elif n == 3:
                    res = ((5*h)/24)*(11*fX[0]+fX[1]+fX[2]+11*fX[3])

                return "La integral en el intervalo [" + str(X[0]) + ", " + str(X[len(X)-1]) + "] es: " + str(res)

