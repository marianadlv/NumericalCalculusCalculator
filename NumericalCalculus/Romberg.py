from sympy import *
import math
import cmath
import numpy as np

class Romberg:

    def __init__(self,funcion,a,b,error):
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
        self.a = eval(a)
        self.b = eval(b)
        self.error = eval(error)

    def solution(self):

        def f(x):
            return eval(self.funcion)

        def trapecio(n):
            a = self.a
            b = self.b
            numPuntos = n

            X = []
            fX = []

            h = (b - a) / numPuntos

            for i in range(numPuntos + 1):
                X.append(a + i * h)
                fX.append(f(X[i]))

            res = 0

            res = res + fX[0] + fX[numPuntos]

            aux = 0

            for i in range(1, numPuntos):
                aux += fX[i]

            res += 2 * aux

            res = res * (h / 2)

            return res

        a = self.a
        b = self.b
        error = self.error

        R = []

        for k in range(0,10):               # límite de 10 --> 2^10
            R.append([])
            R[k].append(trapecio(2 ** k))

            for j in range(2,k+2):
                #print("R[k][j-2]",R[k][j-2],"R[k-1][k-2]",R[k-1][j-2])
                Rk = R[k][j-2] + ( (R[k][j-2] - R[k-1][j-2]) / (4**(j-1) - 1) )
                R[k].append(Rk)

            if k>0:
                #print("Rk: ",R[k][k]," k: ",k,"error: ",abs(R[k][k] - R[k-1][k-1]))
                #print("error",abs(R[k][k] - R[k-1][k-1]),"n",2**k)
                res = ""
                if abs(R[k][k] - R[k-1][k-1]) <= error:
                    for i in range(len(R)):
                        #print("k:",i, end = ' ')
                        res += "k: " + str(i)
                        for j in range(len(R[i])):
                            res += str(round(R[i][j],6)) + ", "
                            #print(round(R[i][j],6), end = ', ')
                        #print()
                        res += "\n"
                    #return "\nLa integral " + self.funcion + " en el intervalo [" + str(a) + ", " + str(b) + "] con un error de " + str(error) + " y una k = " + str(k) + " es: " + str(R[k][k])
                    res += "\nLa integral " + self.funcion + " en el intervalo [" + str(a) + ", " + str(b) + "] con un error de " + str(error) + " y una k = " + str(k) + " es: " + str(R[k][k])
                    return res

        res = ""
        for i in range(len(R)):
            res += "k: " + str(i)
            #print("k:", i, end = ' ')
            for j in range(len(R[i])):
                res += str(round(R[i][j], 6)) + ", "
                #print(round(R[i][j], 6), end = ', ')
            res += "\n"
            #print()
        """return "\nLa integral " + self.funcion + " en el intervalo [" + str(a) + ", " + str(b) + "] con un error de " + str(
            error) + ", una k = " + str(k) + " y una tolerancia de " + str(abs(R[k][k] - R[k-1][k-1])) + " es: " + str(R[k][k])"""
        res += "\nLa integral " + self.funcion + " en el intervalo [" + str(a) + ", " + str(b) + "] con un error de " + str(error) + ", una k = " + str(k) + " y una tolerancia de " + str(abs(R[k][k] - R[k-1][k-1])) + " es: " + str(R[k][k])
        return res


