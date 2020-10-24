import math
from sympy import *
import numpy as np


class NewtonR:
    def __init__(self,fx,p_0,tol):

        self.gx = str(diff(fx))

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

        self.p_0 = eval(p_0)
        self.tol = eval(tol)

    def f(self, x):
        return eval(self.fx)

    def g(self, x):
        return eval(self.gx)

    def solution(self):
        if self.f == "" or self.g == "" or self.p_0 == "" or self.tol == "":
            return "Ingresa datos completos"
        p_0 = self.p_0
        result = ""
        try:
          it = 0
          while True:
            p = p_0 - (self.f(p_0)/self.g(p_0))
            if abs(p-p_0)<self.tol:
              return "La raíz es: " + str(p) + " con una tolerancia de " + str(self.tol) + "\nNúmero de iteraciones: " + str(it)   
            it += 1
            p_0 = p
        except ZeroDivisionError:
            return "División / 0"
        except SyntaxError:
            return "Sintaxis Inválido"


