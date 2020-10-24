import math

class Funcion:
    def __init__(self, fx, x):
        self.fx = fx
        self.x = eval(x)

    def f(self, x):
        return eval(self.fx)

    def Calculate(self):
        try:
            value = self.f(self.x)
            return "f("+str(self.x)+") : "+str(value)
        except ZeroDivisionError:
            return "Zero Division"
        except SyntaxError:
            return "Invalid Syntax"

