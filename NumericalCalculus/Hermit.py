from sympy import *
import math
import cmath
import numpy as np

class Hermit:

    def __init__(self,numPuntos,xi,fi,f1i,punto):
        self.numPuntos = eval(numPuntos)
        self.xi = []
        self.fi = []
        self.f1i = []
        for i in range(self.numPuntos):
            self.xi.append(eval(xi[i]))
            self.fi.append(eval(fi[i]))
            self.f1i.append(eval(f1i[i]))
        if punto!="": self.punto = eval(punto)
        else: self.punto = punto

    def solution(self):

        def fun(x):
            return eval(funcion)

        def f(x,i):
            return eval(str(l1i[i]))

        def p(x):
            return eval(poli)

        #funcion = input("Escribe la función: ")

        numPuntos = self.numPuntos
        xi = self.xi
        fi = self.fi
        f1i = self.f1i

        punto = self.punto

        # sacar Li

        li = []
        l1i = []        # derivadas de Li
        hi = []
        h1i = []        # H gorrito
        poli = ""

        for i in range(numPuntos):
            l = ""
            for j in range(numPuntos):
                if j != i:
                    if l=="": l = "(x-("+str(xi[j])+"))/("+str(xi[i])+"-("+str(xi[j])+"))"
                    else: l = l + "* ( (x-("+str(xi[j])+"))/("+str(xi[i])+"-("+str(xi[j])+")) )"
            li.append(expand(l))
            l1i.append(diff(l))

            # Sacar Hi

            h = "( 1+(-2)*(x-("+str(xi[i])+"))*("+str(f(xi[i],i))+") )*( ("+str(li[i])+")**2 ) *("+str(fi[i])+")"
            hi.append(expand(h))
            h = "(x-("+str(xi[i])+"))*(("+str(li[i])+")**2) *("+str(f1i[i])+")"
            h1i.append(expand(h))
            if poli!= "": poli = poli + "+(" + str(hi[i]) +  ")+(" + str(h1i[i]) + ")"
            else: poli = poli + "(" + str(hi[i]) +  ")+(" + str(h1i[i]) + ")"

        #poli = simplify(poli)
        poli = expand(poli)
        poli = str(poli)

        res = "El polinomio es:\n\n" + str(poli)
        if punto != "" : res += "\n\nP(" + str(punto) + ") = " + str(p(punto))

        return res
