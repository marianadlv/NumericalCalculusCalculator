import math
import numpy as np
from prettytable import PrettyTable


class Secante:
    def __init__(self, f, p_0, p_1, tol,type):
        replacements = {
            'sin': 'math.sin',
            'cos': 'math.cos',
            'log': 'np.log',
            'exp': 'math.exp',
            'sqrt': 'math.sqrt',
            '^': '**',
        }

        for old, new in replacements.items():
            f = f.replace(old, new)

        self.function = f
        self.p_0 = eval(p_0)
        self.p_1 = eval(p_1)
        self.tol = eval(tol)
        self.type = type

    def f(self, x):
        return eval(self.function)

    def solution(self):
        if self.function == "" or self.p_0 == "" or self.p_1 == "" or self.tol == "":
            return "Ingresa datos completos"
        try:
            result = ""
            p_0 = self.p_0
            p_1 = self.p_1
            it = 0

            while True:
                p = p_1 - (self.f(p_1) * (p_1 - p_0) / (self.f(p_1) - self.f(p_0)))
                if abs(p - p_1) < self.tol:
                    result = result + "La raíz es: " + str(p) + " con una tolerancia de " + str(
                        self.tol) + "\nNúmero de iteraciones: " + str(it)
                    if self.type == "1": return result
                    else: return str(p)
                it += 1
                aux = p_1
                p_1 = p
                p_0 = aux

        except ZeroDivisionError:
            return "División / 0"
        except SyntaxError:
            return "Sintaxis inválido"

t0 = 25
q = 300
alpha = 0.04
k = 1
t = 120
beta = 2
x = 1

f = "-"+str(t)+" + "+str(t0)+" + ("+str(q)+"/"+str(k)+")*("+str(beta)+"*( "+str(alpha)+"*"+str(t)+"/math.pi )**(1/2) * exp(-"+str(x)+"**2/(4*"+str(alpha)+"*x)))"
print("Ejercicio 2.47")
print(Secante(f,"1","2","1e-5","1").solution())
print()

print("Ejercicio 2.48")
Re = 6000
f = "-1 + (4*x)/(0.4**0.75) * log("+str(Re)+"*x**(1-0.5*0.4)) - 0.4*x/(0.4**1.2)"
print(Secante(f,"1","2","1e-5","1").solution())
print()

print("Ejercicio 2.49")

Re = 1e4

"""t = PrettyTable(['i','t_i', 'w_i'])
for i in range(len(ti)):
    t.add_row([i, ti[i], wi[i]])
print(t)"""

t = PrettyTable(['Re','f'])
f = "-1/x - 0.4 + 1.74*log("+str(Re)+"*sqrt(x))"

while Re<=1e6:

    f = "-1 - 0.4*x + 1.74*x*log(" + str(Re) + "*sqrt(x))"
    t.add_row([Re,Secante(f,"1","2","1e-5","2").solution()])

    Re += 1e4

print(t)

print()

print("Ejercicio 2.50")

f = "-1.564e6*x + 1e6*x*exp(x) + (0.435e6)*(exp(x)-1)"
print(Secante(f,"1","2","1e-3","1").solution())
print()



