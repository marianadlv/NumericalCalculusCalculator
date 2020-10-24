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

print("Ejercicio 1")
print()

print(Hermit("6",["-40","-20","10","70","100","120"],["1250","1280","1350","1480","1580","1700"],["1.2","1.57","2.87","3.367","3.3","6"],"").solution())
print()

print("Ejercicio 2")
print()
print(Hermit("9",["10","15","20","25","40","50","55","60","75"],["4","20","18","50","33","48","80","60","78"],["0.155","0.213","0.219","0.789","-0.215","2.125","-2.97","1.105","1.235"],"30").solution())
print()

print("Ejercicio 3")
print()

puntos = ["0.2","1.1","1.4","1.9"]

for item in puntos:

    print("Para i =",item)
    print(Hermit("5",["0.25","0.75","1.25","1.5","2.0"],["-0.45","-0.6","0.70","1.88","6.0"],["-0.015","2.25","3.978","3.987","34.652"],item).solution())
    print()

print("Se puede observar que los resultados son factibles. El primer resultado es negativo como debería ser y conforme cambian los puntos, las aproximaciones suben y bajan conforme a la curva formada por los puntos originales.")

print("Ejercicio 4\n")

puntos = ["0.22","0.3","0.45"]

for item in puntos:

    print("Para i =",item)
    print(Hermit("5",["0","0.1250","0.25","0.375","0.5"],["0","6.2402","7.7880","4.8599","0"],["6.2326","7.589","-8.953","-5.785","-3.765"],item).solution())
    print()

print("Ejercicio 5\n")

print(Hermit("6",["-1","-0.5","-0.25","0.25","0.50","1"],["-193","-41","-13.5625","13.5625","41","193"],["1.125","1.015","0.678","-0.258","-0.968","-1.759"],"0.10").solution())
print()

print(Hermit("2",["-0.25","0.25"],["-13.5625","13.5625"],["0.678","-0.258"],"0.10").solution())




