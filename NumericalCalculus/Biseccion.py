import math
import numpy as np

class Biseccion:

    def __init__ (self,fx,tol,left,right):
        replacements = {
            'sin': 'math.sin',
            'cos': 'math.cos',
            'log': 'np.log',
            'exp': 'math.exp',
            'sqrt': 'math.sqrt',
            '^': '**',
        }

        for old, new in replacements.items():
            fx = fx.replace(old, new)

        self.fx = fx
        self.tol = eval(tol)
        self.a = eval(left)
        self.b = eval(right)
    
    def f(self, x):
        return eval(self.fx)

    def function(self, a, b):
        Pm = (a + b)/2
        if self.f(Pm)*self.f(b) < 0:
            a = Pm
        else:
            b = Pm
        return a, b, Pm

    def solution(self):
        if self.function == "" or self.a == "" or self.b == "" or self.tol == "":
            return "Ingresa datos completos"
        result = ""
        try:
            if not(self.f(self.a)*self.f(self.b) < 0):
                return "No hay cambio de signo --> no hay raíces"
            result = result + "En un intervalo ["+ str(self.a) + ", " + str(self.b) + "] con una tolerancia de " + str(self.tol) + "\n"

            it = 0
            a = self.a
            b = self.b
            fa = self.f(a)
            error = 1

            while error > self.tol:
                p = a + ( (b-a)/2 )
                fp = self.f(p)
                error = abs((b-a)/2)
                it += 1
                if fa*fp > 0:
                    a = p
                    fa = fp
                else: b = p

            result = result + "La raíz es: " + str(p) + "\nNúmero de iteraciones: " + str(it)
            return result

        except ZeroDivisionError:
            return "División / 0"
        except SyntaxError:
            return "Sintaxis inválido"



