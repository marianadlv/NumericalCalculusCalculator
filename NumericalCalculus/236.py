from sympy import *
import math
import cmath

class Muller:

    def __init__(self,grado,coef,x0="0",x1="0",x2="0",tol="0"):
        self.grado = eval(grado)
        self.coef = []
        for num in coef:
            self.coef.append(eval(num))
        self.x0 = eval(x0)
        self.x1 = eval(x1)
        self.x2 = eval(x2)
        self.tol = eval(tol)

    def solution(self):

        def f(x):
            return eval(poli)

        grado = self.grado

        coef = self.coef
        poli = ""
        newCoef = []

        # Pedir polinomio

        for i in range(0, grado+1):
            if poli == "": poli = poli + "(" + str(coef[i]) + ")*x**" + str(i)
            else: poli = poli + "+" + "(" + str(coef[i]) + ")*x**" + str(i)
            newCoef.append(0)

        # Pedir otros datos

        #print("Polinomio: ",poli)

        x0 = self.x0
        x1 = self.x1
        x2 = self.x2
        tol = self.tol

        #print("tol: ",tol)
        soluciones = grado

        roots = []
        it = 0

        try:

            while soluciones > 0:

                while it < 1000:

                    it+=1

                    f0 = f(x0)
                    f1 = f(x1)
                    f2 = f(x2)

                    #print("x0: ",x0,"x1: ",x1,"x2: ",x2)

                    a = ( (x1-x2) * (f0-f2) - (x0-x2) * (f1-f2) ) / ( (x0-x2)*(x1-x2)*(x0-x1) )

                    b = ( ((x0-x2)**2) * (f1-f2) - ((x1-x2)**2) *(f0-f2) ) / ( (x0-x2)*(x1-x2)*(x0-x1) )

                    c = f2

                    #print("a: ",a,"b: ",b, "c: ",c)

                    #print("signo: ",b/abs(b))

                    x3 = (-2*c)/( b + (b/abs(b))*cmath.sqrt(b**2 - 4*a*c) ) + x2

                    #print("x3: ",x3, "f(x3): ",f(x3))

                    if abs(f(x3)) < tol:

                        roots.append(x3)
                        #print("raíces: ",roots)

                        newCoef[len(coef)-1] = coef[len(coef)-1]   # b_n = a_n

                        for i in range(len(coef)-2,0,-1):          # desde b_(n-1)
                            newCoef [i] = coef[i] + newCoef[i+1]*x3

                        # crear polinomio otra vez

                        poli = ""

                        newCoef.pop(0)

                        coef = newCoef

                        grado -= 1

                        for i in range(0, grado+1):
                            if poli == "": poli = poli + "(" + str(coef[i]) + ")*x**" + str(i)
                            else: poli = poli + "+" + "(" + str(coef[i]) + ")*x**" + str(i)

                        x0 = x1
                        x1 = x2
                        x2 = x3

                        break

                    x0 = x1
                    x1 = x2
                    x2 = x3
                #print(it)
                soluciones -= 1

            returnSolution = "Raíces:\n "
            for item in roots:
                returnSolution += "\n"+str(item)

            return returnSolution

        except ZeroDivisionError:
            return "División entre 0. Intente otros puntos."
        except SyntaxError:
            return "Sintaxis inválido"

class Volumen:

    def __init__(self,A0,B0,a,b,c):

        self.p = 50
        self.T = 373.15
        self.R = 0.08205746
        self.beta = self.R*self.T*B0 - A0 - self.R*( (c*10000)/self.T**2 )
        self.gamma = -self.R*self.T*B0*b + A0*a - self.R*B0*( (c*10000)/self.T**2 )
        self.delta = self.R*B0*b*( (c*10000)/self.T**2 )

        #ecuación
        # 0 = -pV^4 + RTV^3 + BV^2 + gammaV + delta

    def solution(self):

        print(Muller("4",[str(self.delta),str(self.gamma),str(self.beta),str(self.R*self.T),str(-self.p)],"1","2","3","1e-5").solution())

print("He")
he = Volumen(0.0216,0.01400,0.05984,0,0.0040)
he.solution()
print()

print("H_2")
h2 = Volumen(0.1975,0.02096,-0.00506,-0.43590,0.0504)
h2.solution()
print()

print("O_2")
o2 = Volumen(1.4911,0.04624,0.02562,0.004208,4.8)
o2.solution()
print()

"""A0 = 0.1975
B0 = 0.02096
a = -0.00506
b = -0.43590
c = 0.0504

p = 50
T = 373.15
R = 0.08205746
beta = R*T*B0 - A0 - R*( (c*10000)/T**2 )
gamma = -R*T*B0*b + A0*a - R*B0*( (c*10000)/T**2 )
delta = R*B0*b*( (c*10000)/T**2 )

print(Muller("4",[str(delta),str(gamma),str(beta),str(R*T),str(-p)],"1","2","3","1e-5").solution())"""