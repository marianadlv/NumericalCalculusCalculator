from sympy import *
import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from difDivididas import *

class TaylorN:

    def __init__(self,taylor,a,b,h,cond):
        self.taylor = taylor
        self.a = eval(a)
        self.b = eval(b)
        self.h = eval(h)
        self.cond = (eval(cond[0]),eval(cond[1]))
        dec = str(self.h).split('.')
        self.numDecimals = len(dec[1])

    def solution(self):

        def T(t,w,h=self.h):
            #symbols = {'t':t,'w':w,'h':self.h}
            #return eval(self.taylor,{'__builtins__':None},symbols)
            return eval(self.taylor)

        t = []
        w = []

        t.append(self.cond[0])
        w.append(self.cond[1])

        i = 0

        while(t[i]<self.b):
            i = i + 1
            t.append(round(t[i-1]+self.h,self.numDecimals))
            w.append(w[i-1]+self.h*T(t[i-1],w[i-1]))

        ta = PrettyTable(['i', 't_i', 'w_i'])
        for i in range(len(t)):
            ta.add_row([i, t[i], w[i]])

        return ta

def graphSolution(t,w):
    plt.figure()
    plt.plot(t,w)
    plt.show()

def f(t):
    return eval(fun)

#taylor = "1+t*math.sin(t*w)+(h/2)*(t**2*(1+t*math.sin(t*w))*math.cos(t*w)+w*t*math.cos(t*w))"
#taylor = "1+t*math.sin(t*w)"
#taylor = "(w*t - w**2)/(t**2) + (h/2)*( w**2/t - w/(t**2) + w - 2*w**2*t + 2*w**3 )"3
# 3.c taylor = "1/(t*(w**2 + w)) + (h/2)*( ((w**2+w)**2 + 2*w + 1)/(-1*t**2*(w**2 + w)) )"
# 3.b orden 4 taylor = "math.sin(t) + math.exp(-t) + (h/2)*(math.cos(t)-math.exp(-t)) + (h**2/6)*( -math.sin(t) + math.exp(-t) ) + (h**3/24)*( -math.cos(t) - math.exp(-t) )"
# 3.d taylor = "(-t*w + (4*t)/(w) + (h/2)*( (t**2-1)*w + 4/w - (16*t**2)/(w**3) ))"
# 3.c orden 2 taylor = "(1/t)*(w**2 + w) + (h/2)*( ((w**2+w)*(2*w))/(t**2) )"
# 3.c orden 4 taylor = "(1/t)*(w**2 + w) + (h/2)*( ((w**2+w)*(2*w))/(t**2) ) + (h**2/6)*( ( (w**2+w)*(6*w**2) )/(t**3) ) + (h**3/24)*( ( ( (w**2+w)*(6*w**2) )/(t**4) ) * (  -3 + (2*w+1)*(12*w)*(w**2+w) ) )"
# 3.a orden 2 taylor = "(w/t)-(w**2/t**2) + (h/2)*( (2*w**3/t**4) - (w**2/t**3) )"
# 3.a orden taylor = "(w/t)-(w**2/t**2) + (h/2)*( (2*w**3/t**4) - (w**2/t**3) ) + (h**2/6)*( (w**2/t**4) - (6*w**4/t**6) ) + (h**3/24)*( (-2*w**2/t**5) - (2*w**3/t**6) + (12*w**4/t**7) + (24*w**5/t**8) )"

# 7
"""taylor = "-9.8 - (1/55)*t**2 + (h/2)*( (98/275)*t + 0.000661157*t**3 )"

#taylor = "(2*w)/t + t**2*math.exp(t) + (h/2)*( (2*w)/t**2 + math.exp(t)*(4*t + t**2) )"
# 5 orden 4 taylor = "(2/t)*w + t**2 * math.exp(t) + (h/2)*( (2*w)/(t**2) + math.exp(t)*(4*t + t**2) ) + (h**2/6)*( math.exp(t)*(t**2 + 6*t+6) ) + (h**3/24)*( math.exp(t)*(t**2 + 8*t + 12) )"

fun = "t**2*(math.exp(t)-math.exp(1))"

t = TaylorN(taylor,0.1,1,0.1,(0,8))
ti,wi = t.solution()"""

"""t = PrettyTable(['i','t_i', 'w_i', 'y(t_i)'])
for i in range(len(ti)):
    t.add_row([i, ti[i], wi[i], f(ti[i])])
print(t)"""

"""t = PrettyTable(['i','t_i', 'w_i'])
for i in range(len(ti)):
    t.add_row([i, ti[i], wi[i]])
print(t)"""

#graphSolution(ti,wi)

"""points = [1.04,1.55,1.97]
evals = []

t = PrettyTable(['t', 'Aproximación', 'y(t)'])
for i in range(len(points)):
    evals.append(difDivididas(len(ti), ti, wi, points[i]).solution())
    fi = f(points[i])
    t.add_row([points[i], evals[i], fi])
print(t)"""
