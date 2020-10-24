import math
import numpy as np


class PosicionFalsa:
    def __init__(self, function, p_0, p_1, tol):
        replacements = {
            'sin': 'math.sin',
            'cos': 'math.cos',
            'log': 'np.log',
            'exp': 'math.exp',
            'sqrt': 'math.sqrt',
            '^': '**',
        }

        for old, new in replacements.items():
            function = function.replace(old, new)

        self.function = function
        self.p_0 = eval(p_0)
        self.p_1 = eval(p_1)
        self.tol = eval(tol)

    def f(self, x):
        return eval(self.function)

    def solution(self):
        if self.function == "" or self.p_0 == "" or self.p_1 == "" or self.tol == "":
            return "Ingresa datos completos"

        p_0 = self.p_0
        p_1 = self.p_1
        it = 0
        
        try:
            res = ""
            if self.f(p_0)*self.f(p_1)>=0: return "Puntos no válidos"
            error = 1
            while error>self.tol:
                p_2 = p_1 - ( self.f(p_1)*( p_1 - p_0 )/( self.f(p_1)-self.f(p_0) ) )
                error = abs(p_2-p_1)
                it+=1
                if self.f(p_2)*self.f(p_1)<0: p_0 = p_1
                p_1 = p_2
            return "La raíz es: " + str(p_2) + " con una tolerancia de " + str(self.tol) + "\nNúmero de iteraciones: " + str(it)

        except ZeroDivisionError:
            return "División entre 0"
        except SyntaxError:
            return "Sintaxis inválido"

