from sympy import *
import math
import cmath
import numpy as np

class Diferenciacion:

    def __init__(self,opcion,X,fX):
        self.opcion = eval(opcion)
        self.X = []
        for num in X:
            self.X.append(eval(num))
        self.fX = []
        for num in fX:
            self.fX.append(eval(num))

    def solution(self):

        opcion = self.opcion
        X = self.X
        fX = self.fX

        if opcion == 1:

            h = abs(X[1] - X[0])

            dif1 = (1/(2*h)) * (-3*fX[0]+4*fX[1]-fX[2])

            return "La primera derivada evaluada en " + str(X[0]) + " es: " + str(dif1)

        elif opcion == 2:

            h = X[2] - X[1]

            dif1 = (1/(2*h)) * (fX[2]-fX[0])
            #dif2 = (1/(h**2)) * (fX[0] - 2*fX[1] + fX[2])

            return "La primera derivada evaluada en " + str(X[1]) + " es: " + str(dif1)
        #"\nLa segunda derivada evaluada en " + str(X[1]) + " es: " + str(dif2)


        elif opcion == 3:

            h = X[1] - X[0]

            dif1 = (1/(12*h)) * ( -25*fX[0] + 48*fX[1] - 36*fX[2] + 16*fX[3] - 3*fX[4] )

            return "La primera derivada evaluada en " + str(X[0]) + " es: " + str(dif1)


        elif opcion == 4:

            h = X[4] - X[3]

            dif1 = (1/(12*h)) * ( fX[0] - 8*fX[1] + 8*fX[3] - fX[4] )

            return "La primera derivada evaluada en " + str(X[2]) + " es: " + str(dif1)
