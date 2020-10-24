from sympy import *
import math
import cmath

class difDivididas:

    def __init__(self,numPuntos,X,fX,punto):
        self.numPuntos = eval(numPuntos)
        self.X = []
        for num in X:
            self.X.append(eval(num))
        self.fX = []
        for num in fX:
            self.fX.append(eval(num))
        if punto != "": self.punto = eval(punto)
        else: self.punto = punto
    def solution(self):
        if self.numPuntos != len(self.X) or self.numPuntos != len(self.fX): return "Número incorrecto de puntos."

        def f(x):
            return eval(poli)

        numPuntos = self.numPuntos
        X = self.X
        fX = self.fX

        punto = self.punto

        grado = numPuntos - 1

        coef = []
        poli = ""
        newCoef = []

        A = []
        A.append(fX[0])         # X_0 = f(X_0)

        # coef y newCoef son arreglos de arreglos: cada posición tendrá 3 valores: la dif. dividad, su mínimo y su máximo
        # coef = fX

        for i in range(numPuntos):
            coef.append([fX[i],i,i])

        for j in range(grado):                  # número de dif. divididas

            newCoef = []

            for i in range(0,len(coef)-1):
                min = coef[i][1]
                max = coef[i+1][2]
                res = (coef[i+1][0] - coef[i][0])/(X[max]-X[min])
                newCoef.append([res,min,max])
            coef = newCoef
            A.append(coef[0][0])

        # Crear polinomio con A

        poli = str(A[0])

        for i in range(1,len(A)):
            poli = poli + "+" + str(A[i])
            for j in range(0,i):
                poli = poli + "*(x-" + str(X[j])+")"

        res = ""

        res = "El polinomio de grado " + str(numPuntos-1) + ":\n\n " + str(poli)

        if punto != "": res += "\n\nf(" + str(punto) + ") = " + str(f(punto))

        return res
