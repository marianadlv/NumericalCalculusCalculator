import math
import numpy as np


class Secante:
    def __init__(self, f, p_0, p_1, tol):
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
                p = p_1 - ( self.f(p_1)*( p_1 - p_0 )/( self.f(p_1)-self.f(p_0) ) )
                if abs(p-p_1) < self.tol:
                    result = result + "La raíz es: " + str(p) + " con una tolerancia de " + str(self.tol) + "\nNúmero de iteraciones: "+ str(it)
                    return result
                it += 1
                aux = p_1
                p_1 = p
                p_0 = aux
            
        except ZeroDivisionError:
            return "División / 0"
        except SyntaxError:
            return "Sintaxis inválido"

