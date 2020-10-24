from sympy import *
import math

class NewtonRa:
    def __init__(self, f, g, p_0, tol):
        self.fx = f
        self.gx = g
        self.p_0 = p_0
        self.tol = tol

    def f(self, x):
        return eval(self.fx)

    def g(self, x):
        return eval(self.gx)

    def solution(self):
        p_0 = self.p_0
        result = ""
        try:
          it = 0
          while it<1000:
            p = p_0 - (self.f(p_0)/self.g(p_0))
            if abs(p-p_0)<self.tol:
              #return "La raíz es: " + str(p) + " con una tolerancia de " + str(self.tol) + "\nNúmero de iteraciones: " + str(it)
                return p
            it += 1
            p_0 = p
          if it == 100:
              return "no solución"
        except ZeroDivisionError:
            return "División / 0"
        except SyntaxError:
            return "Sintaxis Inválido"


class Horner:

    def __init__(self,grado,coef,p0="0",tol="0"):
        self.grado = eval(grado)
        self.coef = []
        for num in coef:
            self.coef.append(eval(num))
        self.p0 = eval(p0)
        self.tol = eval(tol)

    def solution(self):

        def f(x):
            return eval(poli)

        grado = self.grado
        coef = self.coef

        poli = ""

        #  Pedir polinomio

        newCoef = []  #  coeficientes b's

        for i in range(0, grado + 1):
            if poli == "":
                poli = poli + "(" + str(coef[i]) + ")*x**" + str(i)
            else:
                poli = poli + "+" + "(" + str(coef[i]) + ")*x**" + str(i)
            newCoef.append(0)

        """print(poli)

        print(newCoef)
        print(coef)"""

        # Pedir otros datos

        p0 = self.p0
        tol = self.tol
        soluciones = grado
        derivada = str(diff(poli))

        cont = 0

        pnArr = []

        while soluciones > 0:
            newton = NewtonRa(poli, derivada, p0, tol)
            pn = newton.solution()
            if pn == "no solución" or pn is None or type(pn) == 'str': break
            elif pn == "División / 0":
                return "División / 0 en Newton Raphson"
            elif pn == "Sintaxis Inválido":
                return "Sintaxis Inválido en Newton Raphson"

            pnArr.append(pn)
            # print(pn)

            soluciones -= 1

            newCoef[len(coef) - 1] = coef[len(coef) - 1]  # b_n = a_n

            for i in range(len(coef) - 2, 0, -1):  # desde b_(n-1)
                newCoef[i] = coef[i] + newCoef[i + 1] * pn

            # crear polinomio otra vez

            poli = ""

            newCoef.pop(0)

            coef = newCoef

            # print(coef)

            grado -= 1

            for i in range(0, grado + 1):
                if poli == "":
                    poli = poli + "(" + str(coef[i]) + ")*x**" + str(i)
                else:
                    poli = poli + "+" + "(" + str(coef[i]) + ")*x**" + str(i)

            # print("new poli", poli)

            derivada = str(diff(poli))

        if len(pnArr)<1: return "Sin raíces reales"
        else:
            text = ""
            for item in pnArr:
                text += str(item) + "\n"
            return "Raíces:\n\n " + text
