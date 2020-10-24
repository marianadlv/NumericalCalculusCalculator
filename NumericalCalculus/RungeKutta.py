from sympy import *
import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

class RungeKutta:

    def __init__(self,funcion,a,b,h,cond):
        self.fun = funcion
        self.a = eval(a)
        self.b = eval(b)
        self.h = eval(h)
        self.cond = (eval(cond[0]), eval(cond[1]))
        dec = str(self.h).split('.')
        self.numDecimals = len(dec[1])

    def solution(self):

        def f(t,w):
            #symbols = {'t':t,'w':w,'h':self.h}
            #return eval(self.taylor,{'__builtins__':None},symbols)
            return eval(self.fun)

        t = []
        w = []

        t.append(self.cond[0])
        w.append(self.cond[1])

        i = 0

        while(t[i]<self.b):
            i = i + 1
            t.append(round(t[i-1]+self.h,self.numDecimals))
            k1 = self.h*f(t[i-1],w[i-1])
            k2 = self.h*f(t[i-1]+(self.h/2), w[i-1] + (k1/2))
            k3 = self.h*f( t[i-1]+(self.h/2), w[i-1] + (k2/2) )
            k4 = self.h*f( t[i]+self.h, w[i-1] + k3 )
            w.append( w[i-1] + (1/6)*(k1+2*k2+2*k3+k4) )

        ta = PrettyTable(['i', 't_i', 'w_i'])
        for i in range(len(t)):
            ta.add_row([i, t[i], w[i]])

        return ta

def graphSolution(t,w):
    plt.figure()
    plt.plot(t,w)
    plt.show()

"""funcion = "t*math.exp(3*t) - 2*w"
#funcion = "w-t**2+1"

t = RungeKutta(funcion,0,1,0.1,(0,0))
#t = RungeKutta(funcion,0,2,0.2,(0,0.5))
ti,wi = t.solution()

t = PrettyTable(['i','t_i', 'w_i'])
for i in range(len(ti)):
    t.add_row([i, ti[i], wi[i]])
print(t)"""

#graphSolution(ti,wi)
