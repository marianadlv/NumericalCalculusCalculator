import math
import numpy as np


class PuntoFijo:
	
   def __init__ (self,f,tol,p_0,a,b):
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
       self.tol = float(eval(tol))
       self.p_0 = float(eval(p_0))
       self.a = eval(a)
       self.b = eval(b)

   def g(self, x):
     return eval(self.function)

   def solution(self):
      if self.function == "" or self.p_0 == "" or self.tol == "":
              return "Ingresa datos completos"

      error = 1
      it = 0
      p_0 = self.p_0
      result = ""

      try:
          #result = result + "En un intervalo [" + str(self.a) + ", " + str(self.b) + "]\n"
          result = ""
          while True:
            try:
              p = self.g(p_0)
              error = abs(p - p_0)
              if error < self.tol:
                result = result + "La raíz es: {:.6f}".format(p) + " con una tolerancia de " + str(self.tol) + "\n"
                if p<self.a or p>self.b: result = result + " --> pero fuera del intervalo [" + str(self.a) + ", " + str(self.b) + "]\n"
                else: result = result + " --> en un intervalo [" + str(self.a) + ", " + str(self.b) + "]\n"
                result = result + "Número de iteraciones: " + str(it)
                return result
              it+=1
              p_0 = p
            except ValueError:
              return "Raíz compleja"
      except ZeroDivisionError:
              return "División / 0"
      except SyntaxError:
              return "Sintaxis Inválido"
      except OverflowError:
              return "Diverge \nÚltima raíz: " + str(p)

