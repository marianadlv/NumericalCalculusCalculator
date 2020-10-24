from sympy import *
import math
import cmath
import numpy as np

class Lagrange:

    def __init__(self,funcion,grado,xi,punto):
        replacements = {
            'sin': 'math.sin',
            'cos': 'math.cos',
            'log': 'np.log',
            'exp': 'math.exp',
            'sqrt': 'math.sqrt',
            '^': '**',
        }

        for old, new in replacements.items():
            funcion = funcion.replace(old, new)

        self.funcion = funcion

        self.grado = eval(grado)
        self.xi = []
        for num in xi:
            self.xi.append(eval(num))
        if punto != "": self.punto = eval(punto)
        else: self.punto = punto

    def solution(self):

        def f(x):
            return eval(funcion)

        """def fError(x):
            return eval(error)"""

        def p(x):
            return eval(poli)

        funcion = self.funcion

        grado = self.grado

        xi = self.xi
        n = grado + 1
        poli = ""
        fi = []
        li = []

        for i in range(n):
            # fi.append( eval(input("f(x_"+str(i)+"): ")) )
            fi.append(f(xi[i]))

        # epsi = eval(input("Cota de derivada n+1: "))
        punto = self.punto

        # sacar Li

        for i in range(n):
            l = ""
            for j in range(n):
                if j != i:
                    if l == "":
                        l = "(x-(" + str(xi[j]) + "))/(" + str(xi[i]) + "-(" + str(xi[j]) + "))"
                    else:
                        l = l + "* ( (x-(" + str(xi[j]) + "))/(" + str(xi[i]) + "-(" + str(xi[j]) + ")) )"
            li.append(l)

        # sumatoria de fi*Li

        for i in range(n):
            if poli == "":
                poli = str(fi[i]) + "*(" + li[i] + ")"
            else:
                poli = poli + "+" + str(fi[i]) + "*(" + li[i] + ")"

        poli = simplify(poli)
        poli = expand(poli)
        poli = str(poli)

        if punto!= "": px = p(punto)
        # fx = f(punto)

        # calcular cota de error

        # error = str(epsi/math.factorial(n))

        # for i in range(n):
        # error = error + "*(x-"+str(xi[i])+")"

        # error = expand(error)
        # error = str(error)

        # print(error)

        # errorNum = abs(fError(punto))
        res = ""
        if punto!= "":
            res = "El polinomio de grado " + str(grado) + " es: \n" + str(poli) + "\n\nP_" + str(grado) + "(" + str(punto) + ") = " + str(px)
        else:
            res = "El polinomio de grado " + str(grado) + " es: \n" + str(poli)

        return res
        # print("f(",punto,") = ",fx)
        # print("El error real es: ", abs(px-fx))
        # print("Cota de error en intervalo [",xi[0],",",xi[len(xi)-1],"]: ",errorNum)

    

