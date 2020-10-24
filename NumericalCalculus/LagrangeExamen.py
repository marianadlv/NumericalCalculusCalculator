from sympy import *
import math
import cmath
import numpy as np

def solution():
    def f(x):
        return eval(funcion)

    def fError(x):
        return eval(error)

    def p(x):
        return eval(poli)

    poli = ""
    fi = []
    li = []

    for i in range(n):
        # fi.append( eval(input("f(x_"+str(i)+"): ")) )
        fi.append(f(xi[i]))

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

    if punto != "":
        px = p(punto)
        fx = f(punto)

    # calcular cota de error

    if epsi != "":

        error = str(epsi/math.factorial(n))

        for i in range(n):
            error = error + "*(x-"+str(xi[i])+")"

        error = expand(error)
        error = str(error)

    # print(error)

        errorNum = abs(fError(puntoError))
    res = ""
    if punto != "":
        print("El polinomio de grado ",str(grado)," es: ",str(poli),"\nP_",str(grado),"(",str(
            punto),") = ",str(px))
        #res = "El polinomio de grado " + str(grado) + " es: " + str(poli) + "\nP_" + str(grado) + "(" + str(punto) + ") = " + str(px)
    else:

        print("El polinomio de grado ",str(grado)," es: ",str(poli))
        #res = "El polinomio de grado " + str(grado) + " es: " + str(poli)

    if epsi != "":

        print("Cota de error en intervalo [",xi[0],",",xi[len(xi)-1],"]: ",errorNum)

    print("f(",punto,") = ",fx)
    print("El error real es: ", abs(px-fx))
    #print("Cota de error en intervalo [",xi[0],",",xi[len(xi)-1],"]: ",errorNum)


funcion = input("Función: ")
grado = eval(input("Grado: "))
n = grado + 1
xi = []
for i in range(n):
    xi.append(eval(input("x_"+str(i)+": ")))
opcion = input("¿Evaluar punto? 1. Sí 2. No\n")
if opcion == "1":
    punto = eval(input("Punto a evaluar: "))
else:
    punto = ""

opcion = input("¿Cota de derivada? 1. Sí 2. No\n")
if opcion == "1":
    epsi = eval(input("Cota de derivada n+1: "))
    puntoError = eval(input("Punto a evaluar: "))
else:
    epsi = ""

solution()

